from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

global host_me
global db_me
global user_me
global passwd_me
global port_me

host_me = "localhost"
db_me = "db_sb"
user_me = "root"
passwd_me = ""
port_me = 3306

class Ui_MainWindow(object):

    #dbconfig
    def connect(self):

        con = pymysql.connect(db=db_me, user=user_me, host=host_me, passwd=passwd_me, port=port_me, autocommit=True)
        cur = con.cursor()
        if (con):
            self.messagebox("Info", "Koneksi Berhasil")
        else:
            self.messagebox("Info", "Koneksi Gagal")

    #messagebox
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setWindowTitle(title)
        mess.setText(message)
        
        # alur
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        result = mess.exec_()

        if result == QtWidgets.QMessageBox.Ok:
            self.open_view()
    
    #view
    def open_view(self):
        view = QtWidgets.QMainWindow()
        self.setupUi(view)
        view.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Tambah Data")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")

        # Label dan input untuk Nama
        self.labelNama = QtWidgets.QLabel(self.centralwidget)
        self.labelNama.setObjectName("labelNama")
        self.labelNama.setText("Nama:")
        self.labelNama.setFixedWidth(50)  # Menetapkan lebar label
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFixedWidth(150) 
        self.plainTextEdit.setFixedHeight(50) 
        self.formLayout.addRow(self.labelNama, self.plainTextEdit)

        # Label dan input untuk Kelas
        self.labelKelas = QtWidgets.QLabel(self.centralwidget)
        self.labelKelas.setObjectName("labelKelas")
        self.labelKelas.setText("Kelas:")
        self.labelKelas.setFixedWidth(50)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setFixedWidth(150)
        self.plainTextEdit_2.setFixedHeight(50) 
        self.formLayout.addRow(self.labelKelas, self.plainTextEdit_2)

        # Label dan input untuk Asal
        self.labelAsal = QtWidgets.QLabel(self.centralwidget)
        self.labelAsal.setObjectName("labelAsal")
        self.labelAsal.setText("Asal:")
        self.labelAsal.setFixedWidth(50)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_3.setFixedWidth(150)
        self.plainTextEdit_3.setFixedHeight(50) 
        self.formLayout.addRow(self.labelAsal, self.plainTextEdit_3)

        # Label dan input untuk Alamat
        self.labelAlamat = QtWidgets.QLabel(self.centralwidget)
        self.labelAlamat.setObjectName("labelAlamat")
        self.labelAlamat.setText("Alamat:")
        self.labelAlamat.setFixedWidth(50)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_4.setFixedWidth(150)
        self.plainTextEdit_4.setFixedHeight(50) 
        self.formLayout.addRow(self.labelAlamat, self.plainTextEdit_4)

        # Label dan input untuk No. HP
        self.labelNoHP = QtWidgets.QLabel(self.centralwidget)
        self.labelNoHP.setObjectName("labelNoHP")
        self.labelNoHP.setText("No. HP:")
        self.labelNoHP.setFixedWidth(50)
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_5.setFixedWidth(150)
        self.plainTextEdit_5.setFixedHeight(50)
        self.formLayout.addRow(self.labelNoHP, self.plainTextEdit_5)

        # Tombol Simpan
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        # Tombol Reset
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.resetButton.setText("Reset")

        self.formLayout.addRow(self.resetButton,self.pushButton)
       # Connect pushButton to insert_data method
        self.pushButton.clicked.connect(self.insert_data)
        # Connect resetButton to reset_inputs method
        self.resetButton.clicked.connect(self.reset_inputs)



        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reset_inputs(self):
        # Mengosongkan semua inputan
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.plainTextEdit_3.clear()
        self.plainTextEdit_4.clear()
        self.plainTextEdit_5.clear()
        self.plainTextEdit.setFocus()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Tambah Data", "Tambah Data"))
        self.pushButton.setText(_translate("MainWindow", "Simpan"))


    def insert_data(self):
        nama = self.plainTextEdit.toPlainText()
        kelas = self.plainTextEdit_2.toPlainText()
        asal = self.plainTextEdit_3.toPlainText()
        alamat = self.plainTextEdit_4.toPlainText()
        no_hp = self.plainTextEdit_5.toPlainText()

        if not (nama and kelas and asal and alamat and no_hp):
            self.messagebox("Error", "Harap isi semua field dengan benar.")
            return
        if not (no_hp.isdigit()):
            self.messagebox("Error", "No HP diisi dengan benar.")
            return
        try:
            con = pymysql.connect(db=db_me, user=user_me, host=host_me, passwd=passwd_me, port=port_me, autocommit=True)
            cur = con.cursor()

            query = "INSERT INTO tb_siswa_baru (nama, kelas, asal, alamat, no_hp) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (nama, kelas, asal, alamat, no_hp))

            self.messagebox("Success", "Data Disimpan")
        except pymysql.Error as e:
            print(f"Error: {str(e)}")
            self.messagebox("Error", f"Terjadi kesalahan: {str(e)}")
        finally:
            con.close()


pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.connect()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    MainWindow.show()
    app.exec_()
