from ultralytics import YOLO
from logger import setup_logger

# Configura o logger
logger = setup_logger(__name__, "model_training")

def train_damage_detection_model():
    """
    Função para treinar o modelo de detecção de danos em contêineres.
    """
    logger.info("--- Iniciando o Treinamento do Modelo de Detecção de Danos ---")
    
    try:
        # Carrega um modelo YOLOv8 pré-treinado. 
        # 'yolov8n.pt' é um bom ponto de partida (pequeno e rápido).
        model = YOLO("yolov8n.pt")
        logger.info("Modelo YOLOv8 pré-treinado ('yolov8n.pt') carregado com sucesso.")
        # Caminho para o arquivo de configuração do dataset
        data_yaml_path = "dataset_Container_Damage_Detection.v1i.yolov8/data.yaml"
        logger.info(f"Usando o arquivo de configuração do dataset: {data_yaml_path}")

        # Inicia o treinamento do modelo
        # - data: aponta para o arquivo de configuração do dataset.
        # - epochs: número de vezes que o modelo verá o dataset completo. 50 é um bom começo.
        # - imgsz: tamanho das imagens para o treinamento. 640 é um padrão comum.
        # - batch: número de imagens processadas por vez. -1 usa um tamanho de lote automático.
        
        logger.info("Iniciando o treinamento. Este processo pode levar algum tempo...")
        model.train(
            data=data_yaml_path,
            epochs=50,
            imgsz=640,
            batch=-1,
            name="yolov8n_damage_detection" # Nome do diretório para salvar os resultados
        )
        
        logger.info("--- Treinamento concluído com sucesso! ---")
        logger.info("O modelo treinado e os resultados foram salvos no diretório 'runs/detect/yolov8n_damage_detection'.")
        logger.info("O melhor modelo está em 'runs/detect/yolov8n_damage_detection/weights/best.pt'.")

    except Exception as e:
        logger.error(f"Ocorreu um erro durante o treinamento: {e}", exc_info=True)

if __name__ == "__main__":
    train_damage_detection_model()
1