from conversor import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import subprocess
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pegar_dir_arquivo_py.clicked.connect(self.abrir_explorador_arquivo_py)
        self.ui.gerar_comando_shell.clicked.connect(self.gerar_comando)
        self.ui.pegar_dir_icon.clicked.connect(self.pegar_dir_icon)
        self.ui.pegar_dir_add_data.clicked.connect(self.pegar_dir_add_data)
        self.ui.resetar_comando_shell.clicked.connect(self.resetar_shell)
        self.ui.executar_comando_shell.clicked.connect(self.executar_shell)
        self.ui.pegar_pasta_ui.clicked.connect(self.abrir_explorador_arquivo_ui)
        self.ui.pushButton_10.clicked.connect(self.gerar_comando_ui)
        self.ui.resetar_shell_ui.clicked.connect(self.resetar_shell2)
        self.ui.executar_shell_ui.clicked.connect(self.executar_shell2)
    
    def abrir_explorador_arquivo_py(self):
        arquivo, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Selecionar Arquivo .py", "", "Arquivos Python (*.py)")
        if arquivo:
            caminho_completo = arquivo[0]
            nome_arquivo = os.path.basename(caminho_completo)  # Pega apenas o nome do arquivo
            diretorio = os.path.dirname(caminho_completo)  # Pega apenas o diretório
            self.ui.dir_exe.setText(diretorio)
            self.ui.dir_py.setText(nome_arquivo)
            
    
    def pegar_dir_icon(self):
        arquivo, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Selecionar Arquivo .ico", "", "Arquivos ICO (*.ico)")
        if arquivo:
            caminho_ico = arquivo[0]
            self.ui.dir_icon.setText(f'{os.path.dirname(caminho_ico)}/{os.path.basename(caminho_ico)}')

    def pegar_dir_add_data(self):
        pasta = QtWidgets.QFileDialog.getExistingDirectory(self, "Selecionar Pasta")
        if pasta:
            self.ui.dir_add_data.setText(pasta)
            

    def gerar_comando(self):
        comando = 'pyinstaller'
        if self.ui.noconfirm.isChecked():
            comando += ' --noconfirm'
        if self.ui.onedir.isChecked():
            comando += ' --onedir'
        if self.ui.windowed.isChecked():
            comando += ' --windowed'
        if self.ui.icon_check.isChecked():
            if self.ui.dir_icon.text():
                diretorio = self.ui.dir_icon.text()
                diretorio_revertido = diretorio.replace("/", "\\")
                comando += f' --icon="{diretorio_revertido}"'
        if self.ui.add_data.isChecked():
            if self.ui.dir_add_data.text():
                diretorio = self.ui.dir_add_data.text()
                diretorio_formatado = os.path.normpath(diretorio)  # Formata o diretório para o sistema operacional
                ultima_pasta = os.path.basename(diretorio_formatado)
                diretorio_invertido = diretorio.replace("\\", "/")
                ultima_barra = diretorio_invertido.rfind("/")
                diretorio_formatado = (
                    diretorio_invertido[:ultima_barra].replace("/", "\\") +
                    "/" +
                    diretorio_invertido[ultima_barra+1:] +
                    f";{ultima_pasta}/"
                )
                comando += f' --add-data="{diretorio_formatado}"'

        if self.ui.dir_exe.text() and self.ui.dir_py.text():
            comando += f' "{self.ui.dir_exe.text()}/{self.ui.dir_py.text()}"'
        self.ui.comando_shell.setText(comando)
    
    def resetar_shell(self):
        self.ui.comando_shell.setText('')

    def resetar_shell2(self):
        self.ui.comando_shell_ui.setText('')

    def executar_shell(self):
        
        comando = self.ui.comando_shell.toPlainText()
        try:
            saida = subprocess.check_output(comando, shell=True, text=True)
            self.ui.logs_executavel.append(saida)
            QtWidgets.QApplication.processEvents()  # Atualiza a interface gráfica
            mensagem_box = QMessageBox()
            mensagem_box.setWindowTitle('Sucesso')
            mensagem_box.setText("Processo concluido")
            mensagem_box.exec_()
        except subprocess.CalledProcessError as e:
            self.ui.logs_executavel.append(f"Erro ao executar o comando: {e}")

    def executar_shell2(self):
        
        comando = self.ui.comando_shell_ui.toPlainText()
        try:
            saida = subprocess.check_output(comando, shell=True, text=True)
            self.ui.logs_executavel.append(saida)
            QtWidgets.QApplication.processEvents()  # Atualiza a interface gráfica
            mensagem_box = QMessageBox()
            mensagem_box.setWindowTitle('Sucesso')
            mensagem_box.setText("Processo concluido")
            mensagem_box.exec_()
        except subprocess.CalledProcessError as e:
            self.ui.logs_executavel.append(f"Erro ao executar o comando: {e}")

    def abrir_explorador_arquivo_ui(self):
        arquivo, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Selecionar Arquivo .UI", "", "Arquivos UI (*.UI)")
        if arquivo:
            caminho_completo = arquivo[0]
            nome_arquivo = os.path.basename(caminho_completo)  # Pega apenas o nome do arquivo
            diretorio = os.path.dirname(caminho_completo)  # Pega apenas o diretório
            self.ui.dir_ui.setText(diretorio)
            self.ui.dir_arquivo_ui.setText(nome_arquivo)

    def gerar_comando_ui(self):
        diretorio = self.ui.dir_ui.text()
        arquivo_ui = self.ui.dir_arquivo_ui.text()
        arquivo_py = self.ui.nome_arquivo_py.text()
        comando = (f'pyuic5 -x "{diretorio}/{arquivo_ui}" -o {arquivo_py}.py')
        self.ui.comando_shell_ui.setText(comando)
        

    
        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
