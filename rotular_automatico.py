import oci
import time

# --- CONFIGURAÇÕES (PREENCHA AQUI) ---
CONFIG_PROFILE = "functions-developer-profile"  # Nome do perfil no seu arquivo .oci/config
DATASET_ID = "ocid1.datalabelingdataset.oc1.sa-saopaulo-1.amaaaaaakm2rzfqar3jcmb6wjdhbrghf63xzrlzwhirwefyuecx6dv4457va" # Cole o OCID do seu Dataset aqui
COMPARTMENT_ID = "ocid1.compartment.oc1..aaaaaaaav3se6eugwjeujk2exs6sf4uitigsl2iwaetkhrpdz7qocyxhonsq" # Cole o OCID do Compartimento aqui


# Mapeamento Exato: "Inicio do nome do arquivo" -> "Rótulo"
# A barra "/" no final da chave é o segredo para não confundir as pastas.
REGRAS_DE_ROTULO = {
    "Dent/": "Dent",
    "Minor-Dent/": "Minor-Dent",
    "Dent-Minor-Dent/": "Dent-Minor-Dent"
}
# ---------------------

def main():
    config = oci.config.from_file(profile_name=CONFIG_PROFILE)
    dls_client = oci.data_labeling_service_dataplane.DataLabelingClient(config)

    print("🔄 Buscando registros sem rótulo...")
    
    # Busca registros paginados
    paginator = oci.pagination.list_call_get_all_results(
        dls_client.list_records,
        compartment_id=COMPARTMENT_ID,
        dataset_id=DATASET_ID,
        is_labeled=False 
    )

    records = paginator.data 
    print(f"📂 Total encontrados: {len(records)}")

    count = 0
    for record in records:
        nome_arquivo = record.name # Ex: Dent/CAIU9370...
        rotulo_escolhido = None

        # Verifica qual regra bate com o início do nome
        for prefixo, label in REGRAS_DE_ROTULO.items():
            if nome_arquivo.startswith(prefixo):
                rotulo_escolhido = label
                break 
        
        if rotulo_escolhido:
            try:
                print(f"[{count+1}] 🏷️ '{nome_arquivo[:20]}...' -> '{rotulo_escolhido}'", end="")
                
                annotation_details = oci.data_labeling_service_dataplane.models.CreateAnnotationDetails(
                    record_id=record.id,
                    compartment_id=COMPARTMENT_ID,
                    entities=[
                        oci.data_labeling_service_dataplane.models.GenericEntity(
                            entity_type="GENERIC",
                            labels=[oci.data_labeling_service_dataplane.models.Label(label=rotulo_escolhido)]
                        )
                    ]
                )

                dls_client.create_annotation(create_annotation_details=annotation_details)
                print(" ✅")
                count += 1
                time.sleep(0.5) # Pausa de segurança para API

            except Exception as e:
                print(f" ❌ Erro: {e}")
        else:
            print(f"⚠️ Ignorado: '{nome_arquivo}' (Pasta desconhecida)")

    print(f"\n🏁 Sucesso! {count} imagens foram rotuladas.")

if __name__ == "__main__":
    main()