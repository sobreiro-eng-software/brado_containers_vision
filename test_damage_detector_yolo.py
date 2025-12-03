import cv2
import os
from damage_detector import ObjectDetector
from logger import setup_logger

# Configura o logger para este módulo
logger = setup_logger(__name__, "test_damage_detector")

# --- Bloco de Teste para Detecção de Danos ---
if __name__ == "__main__":
    logger.info("--- Iniciando teste do Detector de Danos em Contêineres ---")

    # Instancia o ObjectDetector com o modelo treinado e a classe de dano
    # NOTA: Você precisará treinar um modelo YOLO com seu dataset.
    # Por enquanto, vou usar 'yolov8n.pt', mas ele não detectará 'Damage'.
    # Troque 'yolov8n.pt' pelo caminho do seu modelo treinado (ex: 'runs/detect/train/weights/best.pt')
    damage_detector = ObjectDetector(
        model_path="yolov8n.pt", 
        detection_class_name="Damage",
        detection_class_id= 0, # ID da classe 'Damage' do seu data.yaml
        confidence_threshold=0.25 # Limiar mais baixo para testes
    )

    # Caminho para uma imagem de teste do dataset
    test_image_path = "Dataset_Conteineres_vision/damaged/container_1.jpg"

    if not os.path.exists(test_image_path):
        logger.error(f"Imagem de teste não encontrada em: {test_image_path}")
    else:
        logger.info(f"Carregando imagem de teste: {test_image_path}")
        sample_image = cv2.imread(test_image_path)

        # Chama o método de detecção
        logger.info("Executando detecção de danos...")
        detection = damage_detector.detect(sample_image)

        # Processa e exibe os resultados
        if detection:
            logger.info(f"Dano detectado: {detection}")
            # Desenha o bbox na imagem para verificação visual
            x1, y1, x2, y2 = map(int, detection["bbox"])
            cv2.rectangle(sample_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(
                sample_image,
                f"{detection['class']} ({detection['confidence']:.2f})",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 0, 255),
                2,
            )
            # Salva a imagem com a detecção para depuração
            cv2.imwrite("debug_damage_detection.jpg", sample_image)
            logger.info("Imagem com detecção salva como 'debug_damage_detection.jpg'")
        else:
            logger.info("Nenhum dano detectado na imagem de exemplo.")

    logger.info("--- Teste concluído ---")
