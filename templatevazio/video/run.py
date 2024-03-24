import os
import json
from moviepy.editor import VideoFileClip

def listar_arquivos(diretorio):
    arquivos = []
    for arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, arquivo)) and not arquivo.endswith('.py') and not arquivo.endswith('.html') and not arquivo.endswith('.json'):
            arquivos.append({
                "nome": arquivo,
                "tamanho_bytes": os.path.getsize(os.path.join(diretorio, arquivo)),
                "duracao_video": obter_duracao_video(os.path.join(diretorio, arquivo))
            })
    return arquivos

def obter_duracao_video(caminho):
    if caminho.endswith('.mp4') or caminho.endswith('.avi') or caminho.endswith('.mov'):
        clip = VideoFileClip(caminho)
        duracao_segundos = clip.duration
        clip.close()
        duracao_formatada = str(int(duracao_segundos // 3600)).zfill(2) + ':' + str(int((duracao_segundos % 3600) // 60)).zfill(2) + ':' + str(int(duracao_segundos % 60)).zfill(2)
        return duracao_formatada
    else:
        return None

def criar_arquivo_json(arquivos):
    with open('dados.json', 'w') as json_file:
        json.dump({"arquivos": arquivos}, json_file, indent=4)

if __name__ == "__main__":
    diretorio = os.getcwd()
    arquivos = listar_arquivos(diretorio)
    criar_arquivo_json(arquivos)
    print("Arquivo dados.json criado com sucesso.")
