# Conversor de Interface UI para Python e de Python para EXE

Este é um programa em Python que permite converter interfaces de usuário criadas com arquivos .ui (criados pelo Qt Designer) em código Python utilizável para aplicações PyQt5. Ele também oferece a funcionalidade de gerar comandos arquivos .exe (executável) a partir de um arquivo .py, possibilitando assim, converter uma .ui para .py e depois para .exe (executável). O programa foi feito pensando em facilitar a criação de intrfaces gráficas usando o QT Design, pois o mesmo gera um arquivo .ui que pode ser convertido para .py, para que assim sejam feitas implementações de funções ou quaisquer alterações.

## Funcionalidades

- Selecionar um arquivo .ui para conversão em código Python.
- Executar os comandos gerados para realizar a conversão e criação do arquivo Python a partir de um .ui usando a ferramenta pyuic5.
- Conversão de interfaces de usuário .ui para código Python usando a ferramenta pyuic5.
- Gerar comandos para transformar o código Python em um executável usando o PyInstaller.
- Opções para personalizar o processo de criação do executável, incluindo ícone e dados adicionais.
- Executar os comandos gerados para realizar a conversão e criação do executável.


## Uso do conversor de .py para .exe
![image](https://github.com/Carlos-Guilherme/Conversor_Pyqt/assets/72580077/c2c589dd-3526-4834-b501-299a4f65e491)

1. **Selecionar Arquivo .py**: Use o botão "Selecionar" na aba "Fazer Executável" para selecionar um arquivo .py existente para a criação do executável.

2. **Opções de Executável**: Marque as opções desejadas para personalizar a criação do executável, como "--noconfirm", "--onedir", "--windowed", "--icon" e "--add-data". Para mais informações sobre como funciona a biblioteca Pyinstaller recomendo olhar a documentação: <a href='https://pyinstaller.org/en/stable/'>Documentação</a>

3. **Gerar Comando**: Pressione o botão "Gerar Comando" para criar o comando que gera um executável a partir do arquivo .py usando o PyInstaller.

4. **Resetar Comando**: Limpa o campo de comando gerado para a criação do executável.

5. **Executar Comando**: Clique neste botão para executar o comando gerado e criar o executável.

6. **Logs**: Esta área exibe os logs e resultados das operações realizadas.

## Uso do conversor de .ui para .py
![image](https://github.com/Carlos-Guilherme/Conversor_Pyqt/assets/72580077/e7a6f0f2-7518-43cd-8eeb-5b0a77c567cf)

1. **Selecionar Arquivo .ui**: Clique no botão "Selecionaar" na aba ".UI para .py" para selecionar um arquivo de interface de usuário (.ui) criado pelo Qt Designer.
2.  **Dê um nome ao arquivo .py a ser gerado**: No campo "Nome do .py" coloque o nome que deseja para o arquivo .py

3. **Gerar Comando UI**: Pressione o botão "Gerar Comando UI" para criar o comando que converte o arquivo .ui em um arquivo .py usando o pyuic5.

4. **Resetar Shell UI**: Este botão limpa o campo de comando gerado para a conversão de UI para Python.

5. **Executar Shell UI**: Clique neste botão para executar o comando gerado e converter o arquivo .ui em um arquivo .py.

## Requisitos

- Python 3.x
- PyQt5
- PyInstaller

Para instalar use: 
```bash
pip install PyQt5 pyinstaller

## Autor

Carlos Guilherme
