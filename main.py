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

    def messageboxvalidasi(self, title, message,aksi,id):
        mess = QtWidgets.QMessageBox()
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setWindowTitle(title)
        mess.setText(message)
        
        # alur
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
        result = mess.exec_()

        if result == QtWidgets.QMessageBox.Ok:
            if(aksi == "delete"):
                self.delete_data(id)
                self.read_data()
            elif(aksi == "update"):
                self.read_data()
        elif result == QtWidgets.QMessageBox.Cancel:
            self.read_data()
    
    #view
    def open_view(self):
        view = QtWidgets.QMainWindow()
        self.setupUi(view)
        view.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Tambah Data")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout Utama
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Layout untuk Tombol
        self.buttonLayout = QtWidgets.QHBoxLayout()

        # Tombol Insert/Create
        self.InsertButton = QtWidgets.QPushButton("Insert")
        self.InsertButton.hide()
        self.buttonLayout.addWidget(self.InsertButton)

        # Tombol Read
        self.ReadButton = QtWidgets.QPushButton("Read")
        self.ReadButton.hide()
        self.buttonLayout.addWidget(self.ReadButton)

        # Tombol Update
        self.UpdateButton = QtWidgets.QPushButton("Update")
        self.UpdateButton.hide()
        self.buttonLayout.addWidget(self.UpdateButton)

        # Tombol Delete
        self.DeleteButton = QtWidgets.QPushButton("Delete")
        self.DeleteButton.hide()
        self.buttonLayout.addWidget(self.DeleteButton)

        # Tambahkan layout tombol ke layout utama
        self.mainLayout.addLayout(self.buttonLayout)

        # Header
        self.headerLabel = QtWidgets.QLabel(self.centralwidget)
        self.headerLabel.setObjectName("headerLabel")
        self.headerLabel.setText("Data Siswa Baru")
        font = self.headerLabel.font()
        font.setPointSize(16)  # Ubah ukuran font sesuai keinginan
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setFixedHeight(30)
        self.headerLabel.setFixedWidth(1400)

        # Tambahkan header label
        self.mainLayout.addWidget(self.headerLabel)

        # Form Layout untuk label dan input
        self.formLayout = QtWidgets.QFormLayout()

        # Input untuk ID update
        self.plainTextEdit_id = QtWidgets.QPlainTextEdit()
        self.plainTextEdit_id.setObjectName("plainTextEdit")
        self.plainTextEdit_id.setFixedWidth(180) 
        self.plainTextEdit_id.setFixedHeight(30) 
        self.plainTextEdit_id.hide()
        self.formLayout.addRow(self.plainTextEdit_id)

        # Label dan input untuk Nama
        self.labelNama = QtWidgets.QLabel()
        self.labelNama.setObjectName("labelNama")
        self.labelNama.setText("Nama:")
        self.labelNama.setFixedWidth(50)
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFixedWidth(180) 
        self.plainTextEdit.setFixedHeight(30) 
        self.formLayout.addRow(self.labelNama, self.plainTextEdit)

        # Label dan input untuk Kelas
        self.labelKelas = QtWidgets.QLabel()
        self.labelKelas.setObjectName("labelKelas")
        self.labelKelas.setText("Kelas:")
        self.labelKelas.setFixedWidth(50)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit()
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setFixedWidth(180)
        self.plainTextEdit_2.setFixedHeight(30) 
        self.formLayout.addRow(self.labelKelas, self.plainTextEdit_2)

        # Label dan input untuk Asal
        self.labelAsal = QtWidgets.QLabel()
        self.labelAsal.setObjectName("labelAsal")
        self.labelAsal.setText("Asal:")
        self.labelAsal.setFixedWidth(50)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit()
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_3.setFixedWidth(180)
        self.plainTextEdit_3.setFixedHeight(30) 
        self.formLayout.addRow(self.labelAsal, self.plainTextEdit_3)

        # Label dan input untuk Alamat
        self.labelAlamat = QtWidgets.QLabel()
        self.labelAlamat.setObjectName("labelAlamat")
        self.labelAlamat.setText("Alamat:")
        self.labelAlamat.setFixedWidth(50)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit()
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_4.setFixedWidth(180)
        self.plainTextEdit_4.setFixedHeight(50) 
        self.formLayout.addRow(self.labelAlamat, self.plainTextEdit_4)

        # Label dan input untuk No. HP
        self.labelNoHP = QtWidgets.QLabel()
        self.labelNoHP.setObjectName("labelNoHP")
        self.labelNoHP.setText("No. HP:")
        self.labelNoHP.setFixedWidth(50)

        # LineEdit untuk input angka
        self.plainTextEdit_5 = QtWidgets.QLineEdit()
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_5.setValidator(QtGui.QIntValidator())
        self.plainTextEdit_5.setFixedWidth(180)
        self.plainTextEdit_5.setFixedHeight(30)
        self.formLayout.addRow(self.labelNoHP, self.plainTextEdit_5)

        # Tombol Simpan
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #150485; color: white;")
        
        # Tombol Reset
        self.resetButton = QtWidgets.QPushButton()
        self.resetButton.setObjectName("resetButton")
        self.resetButton.setText("Reset")
        self.resetButton.setStyleSheet("background-color: #FF9300; color: white;")

        self.pushButton.clicked.connect(self.btn_cek_aksi)
        
        self.formLayout.addRow(self.resetButton, self.pushButton)

        self.resetButton.clicked.connect(self.reset_inputs)

        self.mainLayout.addLayout(self.formLayout)

        # Table Widget untuk menampilkan data
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7) 
        header_labels = ['id','Nama', 'Kelas', 'Asal', 'Alamat', 'No. HP','Aksi']
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.mainLayout.addWidget(self.tableWidget)
        self.tableWidget.setColumnHidden(0, True)

        self.read_data()

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
        self.plainTextEdit_id.clear()
        self.plainTextEdit.setFocus()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Tambah Data", "Tambah Data"))
        self.pushButton.setText(_translate("MainWindow", "Simpan"))

    def btn_cek_aksi(self):
        id_sb = self.plainTextEdit_id.toPlainText()
        if id_sb:
            self.update_data_aksi(id_sb)
        else:
            self.insert_data

    def insert_data(self):

        nama = self.plainTextEdit.toPlainText()
        kelas = self.plainTextEdit_2.toPlainText()
        asal = self.plainTextEdit_3.toPlainText()
        alamat = self.plainTextEdit_4.toPlainText()
        no_hp = self.plainTextEdit_5.text()

        if not (nama and kelas and asal and alamat and no_hp):
            self.messagebox("Gagal", "Harap isi semua field dengan benar.")
            return
        if not (no_hp.isdigit()):
            self.messagebox("Gagal", "No HP diisi dengan benar.")
            return
        try:
            con = pymysql.connect(db=db_me, user=user_me, host=host_me, passwd=passwd_me, port=port_me, autocommit=True)
            cur = con.cursor()

            query = "INSERT INTO tb_siswa_baru (nama, kelas, asal, alamat, no_hp) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (nama, kelas, asal, alamat, no_hp))

            self.reset_inputs()
            self.read_data()
            self.messagebox("Behasil", "Data Disimpan")
        except pymysql.Error as e:
            print(f"Gagal: {str(e)}")
            self.messagebox("Gagal", f"Terjadi kesalahan: {str(e)}")
        finally:
            con.close()

    def read_data(self):
        try:
            con = pymysql.connect(db=db_me, user=user_me, host=host_me, passwd=passwd_me, port=port_me, autocommit=True)
            cur = con.cursor()
            cur.execute("SELECT DISTINCT * FROM tb_siswa_baru")
            data = cur.fetchall()
            if data:
                self.tableWidget.setRowCount(0)
                for row_num, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_num)
                    for col_num, col_data in enumerate(row_data):
                        self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

                    # Menambahkan tombol pada kolom aksi
                    action_widget = QtWidgets.QWidget()
                    layout = QtWidgets.QHBoxLayout()
                                        
                    update_button = QtWidgets.QPushButton("Update")
                    update_button.setMaximumWidth(200)
                    update_button.setStyleSheet("background-color: #03C4A1; color: white;")
                    update_button.clicked.connect(lambda _, id=str(row_data[0]):self.update_data(id))

                    delete_button = QtWidgets.QPushButton("Delete")
                    delete_button.setMaximumWidth(200)
                    delete_button.setStyleSheet("background-color: #C62A88; color: white;")
                    
                    delete_button.clicked.connect(lambda _, id=str(row_data[0]): self.messageboxvalidasi("Perhatian","Yakin ingin menghapus data?","delete",id)) 

                    layout.setContentsMargins(0, 0, 0, 0)
                                        
                    layout.addWidget(update_button)
                    layout.addWidget(delete_button)
                                        
                    action_widget.setLayout(layout)
                                        
                    self.tableWidget.setCellWidget(row_num, len(row_data), action_widget)

            # else:
            #     self.messagebox("Info", "Data tidak ditemukan")
        except pymysql.Error as e:
            error_message = f"Gagal: {str(e)}"
            print(error_message) 
            self.messagebox("Gagal", f"Terjadi kesalahan: {str(e)}")
        finally:
            con.close()

    def delete_data(self, id):
        try:
            con = pymysql.connect(db=db_me, user=user_me, host=host_me, passwd=passwd_me, port=port_me, autocommit=True)
            cur = con.cursor()
            cur.execute("DELETE FROM tb_siswa_baru WHERE id_sb = %s", (id,))
            self.read_data() 
            self.messagebox("Behasil", "Data Terhapus")
        except pymysql.Error as e:
            error_message = f"Gagal: {str(e)}"
            print(error_message) 
            self.messagebox("Gagal", f"Terjadi kesalahan: {str(e)}")
        finally:
            con.close()

    def update_data(self, id):
        try:
            con = pymysql.connect(db=db_me, user=user_me, host=host_me, passwd=passwd_me, port=port_me, autocommit=True)
            cur = con.cursor()
            cur.execute("SELECT * FROM tb_siswa_baru WHERE id_sb = %s", (id,))
            row = cur.fetchone()

            if row:
                id_sb = str(row[0])
                nama = row[1]
                kelas = row[2]
                asal = row[3]
                alamat = row[4]
                no_hp = row[5]

            self.plainTextEdit_id.setPlainText(id_sb)
            self.plainTextEdit.setPlainText(nama)
            self.plainTextEdit_2.setPlainText(kelas)
            self.plainTextEdit_3.setPlainText(asal)
            self.plainTextEdit_4.setPlainText(alamat)
            self.plainTextEdit_5.setText(no_hp)
            self.read_data() 

        except pymysql.Error as e:
            error_message = f"Gagal: {str(e)}"
            print(error_message) 
            self.messagebox("Gagal", f"Terjadi kesalahan: {str(e)}")
        finally:
            con.close()

    def update_data_aksi(self, id):
        try:
            con = pymysql.connect(db=db_me, user=user_me, host=host_me, passwd=passwd_me, port=port_me, autocommit=True)
            cur = con.cursor()

            nama = self.plainTextEdit.toPlainText()
            kelas = self.plainTextEdit_2.toPlainText()
            asal = self.plainTextEdit_3.toPlainText()
            alamat = self.plainTextEdit_4.toPlainText()
            no_hp = self.plainTextEdit_5.text()

            cur.execute("UPDATE tb_siswa_baru SET nama=%s, kelas=%s, asal=%s, alamat=%s, no_hp=%s WHERE id_sb = %s",
            (nama, kelas, asal, alamat, no_hp, id))

            self.reset_inputs()
            self.read_data()
            self.messagebox("Behasil", "Data Diperbarui") 

        except pymysql.Error as e:
            error_message = f"Gagal: {str(e)}"
            print(error_message) 
            self.messagebox("Gagal", f"Terjadi kesalahan: {str(e)}")
        finally:
            con.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.connect()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
