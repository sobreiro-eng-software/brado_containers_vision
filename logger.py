import logging
import os


def setup_logger(logger_name, log_dir_name):
    """
    Configura e retorna um logger com handlers de arquivo e console, evitando duplicação.

    :param logger_name: O nome do logger (geralmente __name__).
    :param log_dir_name: O nome do subdiretório dentro de 'logs' para o arquivo de log.
    :return: Uma instância do logger configurado.
    """
    # Cria um logger específico
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Se o logger já tiver handlers, retorna a instância existente para evitar duplicação
    if logger.hasHandlers():
        return logger

    # Define o diretório e o nome do arquivo de log
    log_dir = os.path.join("logs", log_dir_name)
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{log_dir_name}.log")

    # Define o formato do log, incluindo o nome da thread
    formatter = logging.Formatter(
        "%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Cria um handler para escrever os logs em um arquivo
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Cria um handler para o console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
