from ultralytics import YOLO

# Caminho ABSOLUTO onde o arquivo last.pt está escondido atualmente.
# Não movemos ele para garantir que o 'resume' funcione perfeitamente.
caminho_checkpoint = "/home/sobreiro/Área de Trabalho/prime_python/cam-capture-brado/runs/detect/yolov8n_damage_detection/weights/last.pt"

print(f"--- RETOMANDO TREINAMENTO ---")
print(f"Carregando checkpoint de: {caminho_checkpoint}")

# Carrega o modelo com os pesos salvos
model = YOLO(caminho_checkpoint)

# O comando resume=True faz a mágica:
# Ele lê o arquivo, vê que parou na época 25 e continua dali.
results = model.train(resume=True)