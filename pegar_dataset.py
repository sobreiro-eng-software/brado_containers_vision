import roboflow

# Autentique-se com o Roboflow (será solicitado na primeira vez)
roboflow.login()

# URL do conjunto de dados que você deseja baixar
# Exemplo para o dataset "car_dent_scratch_detection"
dataset_url = "https://universe.roboflow.com/sindhu/car_dent_scratch_detection-1/9"

# Faça o download do dataset no formato desejado (ex: COCO, YOLOv5, etc. )
roboflow.download_dataset(
    dataset_url=dataset_url,
    model_format="coco"  # ou "yolov5", "yolov8", "tfrecord", etc.
)