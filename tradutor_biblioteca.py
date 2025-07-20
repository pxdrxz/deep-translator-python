from deep_translator import GoogleTranslator

def traduzir(texto, origem='auto', destino='en'):
    try:
        traducao = GoogleTranslator(source=origem, target=destino).translate(texto)
        return traducao
    except Exception as e:
        return f"Erro: {e}"

if __name__ == "__main__":
    print("=== Tradutor (Biblioteca) ===")
    texto = input("Digite o texto para traduzir: ")
    idioma_destino = input("Idioma destino (ex: en, es, fr, pt): ")
    print("Tradução:", traduzir(texto, destino=idioma_destino))

    