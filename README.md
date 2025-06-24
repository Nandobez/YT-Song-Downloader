-----

# Download de Áudio com `yt-dlp`

Este é um script Python simples que utiliza a ferramenta de linha de comando `yt-dlp` para baixar o áudio de vídeos de diversas plataformas (como YouTube, Vimeo, etc.) e convertê-los para o formato MP3.

-----

## Funcionalidades

  * Baixa apenas o áudio de um link fornecido.
  * Converte o áudio baixado para **MP3**.
  * Salva o arquivo com o título original do vídeo.
  * Fornece feedback sobre o processo de download.

-----

## Requisitos

Antes de usar este script, você precisa ter o **Python** instalado em sua máquina e a ferramenta **`yt-dlp`**.

### 1\. Instalar Python

Se você ainda não tem Python, pode baixá-lo e instalá-lo a partir do site oficial: [python.org](https://www.python.org/downloads/)

### 2\. Instalar `yt-dlp`

`yt-dlp` é uma ferramenta de linha de comando. Você pode instalá-la de várias maneiras, mas a mais comum é usando `pip` (gerenciador de pacotes do Python) ou `Homebrew` (para macOS).

**Usando `pip` (recomendado):**

Abra seu terminal ou prompt de comando e execute:

```bash
pip install yt-dlp
```

**Para usuários macOS (usando Homebrew):**

Se você tem o Homebrew instalado, pode instalar `yt-dlp` com:

```bash
brew install yt-dlp
```

-----

## Como Usar

1.  **Salve o Código:**
    Copie o código fornecido e salve-o em um arquivo com extensão `.py`, por exemplo, `baixar_audio.py`.

2.  **Execute o Script:**
    Abra seu terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute o script Python:

    ```bash
    python baixar_audio.py
    ```

3.  **Insira o Link:**
    O script pedirá que você digite o link do vídeo. Cole o link e pressione `Enter`:

    ```
    Digite o link em questão: [COLE SEU LINK AQUI E PRESSIONE ENTER]
    ```

    O download será iniciado e, ao final, o arquivo MP3 estará salvo na mesma pasta onde você executou o script.

-----

## Exemplo de Uso

```bash
# Na linha de comando
python baixar_audio.py
```

```
Digite o link em questão: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Após a conclusão, um arquivo MP3 com o título do vídeo será criado na pasta atual.

-----

## Solução de Problemas

  * **`yt-dlp` não encontrado:** Certifique-se de que `yt-dlp` foi instalado corretamente e que seu diretório de instalação está no `PATH` do sistema. Se você instalou com `pip`, ele geralmente cuida disso.
  * **Erro de download:** Verifique se o link que você forneceu é válido e se o vídeo ainda está disponível. Alguns vídeos podem ter restrições que impedem o download.
  * **Problemas de permissão:** Certifique-se de que o script tem permissão para gravar arquivos no diretório onde está sendo executado.

-----
