from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import MySQLdb
import datetime
 

ui, _ = loadUiType('Biblio.ui')
login,_ = loadUiType('Login.ui')


class Login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        
        
        
        
        
    def Handel_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        #La création de l'objet cursor pour interagir avec la bdd, pour exécuter des requêtes SQL
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Enterd Your Username And Password Correctly')  

    

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()

        self.Handel_Buttons()
        self.Show_Category()
        self.Show_Author()

        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_All_Books()
        self.Show_All_Operations()

    
    def Handel_Buttons(self):
        
        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)
        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_16.clicked.connect(self.Add_Category)
        self.pushButton_17.clicked.connect(self.Add_Author)
        self.pushButton_12.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Books)
        self.pushButton_11.clicked.connect(self.Delete_Books)
        self.pushButton_6.clicked.connect(self.Handel_Day_Operations)
        self.pushButton_13.clicked.connect(self.Add_New_User)
        self.pushButton_14.clicked.connect(self.Login)
        self.pushButton_15.clicked.connect(self.Edit_User)



    def Handel_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)

        """------- Open tabs ------- """

    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)


    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)
        
        
        
        """------- Days Operations ------- """
        
    def Handel_Day_Operations(self):
        book_title = self.lineEdit.text()
        client_name = self.lineEdit_28.text()
        type = self.comboBox.currentText()
        days_number = self.comboBox_2.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days_number)
             
        print(today_date)
        print(to_date)

        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='bibliotheque')
        self.cur = self.db.cursor()

        self.cur.execute("SELECT * FROM book WHERE Book_name = %s", (book_title,))
        book_exists = self.cur.fetchone()
        
        if not book_exists:
            QMessageBox.warning(self, "Book Not Found", "This book's title doesn't exist")
        
        else:
            if type == "retrieve":
                   
                   self.cur.execute('''
                   INSERT INTO day(book_name, client, type  , date , return_date )
                   VALUES (%s , %s , %s , %s , %s)
                   ''' , (book_title ,client_name, type  , today_date  , today_date))
                   
                   self.db.commit()
                   

                   self.statusBar().showMessage('New Operation Added')
                   self.Show_All_Operations()
            else :
                  
                  self.cur.execute('''
                  INSERT INTO day(book_name, client, type , date , to_date, due_date )
                  VALUES (%s , %s , %s, %s , %s , %s )
                  ''' , (book_title ,client_name, type , today_date  , to_date, to_date ))

                  self.db.commit()
                  self.statusBar().showMessage('New Operation Added')
                  self.Show_All_Operations()
        
        
    def Show_All_Operations(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='bibliotheque')
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , client , type , date , to_date,due_date, return_date  FROM day
        ''')

        data = self.cur.fetchall()

        #Supprimer toutes les lignes
        self.tableWidget.setRowCount(0)
        #Ajouter une ligne vide 
        self.tableWidget.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1
            #Avoir_le_nombre_total_de_ligne
            row_position = self.tableWidget.rowCount()
            #Ajouter_une_ligne_vide
            self.tableWidget.insertRow(row_position)


        
        """------- Books ------- """

    def Show_All_Books(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='bibliotheque')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_code,book_name,category,book_Author,book_Price FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)

        self.db.close()   





    def Add_New_Book(self):
        
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor()
        
        book_title = self.lineEdit_3.text()
        book_code = self.lineEdit_2.text()
        book_category = self.comboBox_6.currentText()
        book_author = self.comboBox_7.currentText()
        book_price = self.lineEdit_4.text()
        
        
        self.cur.execute('''
            INSERT INTO book(Book_name,Book_code,category,Book_Author,Book_Price)
            VALUES (%s , %s , %s , %s  , %s)
        ''' ,(book_title , book_code , book_category , book_author  , book_price))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_3.setText('')
        self.lineEdit_2.setText('')
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.lineEdit_4.setText('')
        self.Show_All_Books()
        
    
    def Search_Books(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()

        sql = ''' SELECT * FROM book WHERE Book_name = %s'''
        self.cur.execute(sql , [(book_title)])

        data = self.cur.fetchone()
       
        if data :    
            print(data)
            self.lineEdit_14.setText(data[1])
            self.lineEdit_6.setText(data[2])
            self.comboBox_13.addItem(data[3])
            self.comboBox_12.addItem(data[4])
            self.lineEdit_7.setText(str(data[5]))
        else :  
            QMessageBox.information(self, "Aucun livre trouvé", "Le titre du livre n'existe pas.")

        
       
        
        
        
    
    
    def Edit_Books(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_14.text()
        book_code = self.lineEdit_6.text()
        book_category = self.comboBox_13.currentText()
        book_author = self.comboBox_12.currentText()
        book_price = self.lineEdit_7.text()


        search_book_title = self.lineEdit_5.text()

        self.cur.execute('''
            UPDATE book SET Book_name=%s ,Book_code=%s ,category=%s ,Book_Author=%s ,Book_Price=%s WHERE Book_name = %s            
        ''', (book_title,book_code,book_category,book_author , book_price , search_book_title))

        self.db.commit()
        self.statusBar().showMessage('book updated')
        self.Show_All_Books()
        
    
    def Delete_Books(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()

        warning = QMessageBox.warning(self , 'Delete Book' , "are you sure you want to delete this book" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM book WHERE Book_name = %s '''
            self.cur.execute(sql , [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

            self.Show_All_Books()
           
    
    """------- Users ------- """
    
    def Add_New_User(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor()

        username = self.lineEdit_15.text()
        email = self.lineEdit_17.text()
        password = self.lineEdit_18.text()
        password2 = self.lineEdit_16.text()

        if password == password2 :
            self.cur.execute(''' 
                INSERT INTO users(user_name , user_email , user_password)
                VALUES (%s , %s , %s)
            ''' , (username , email , password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_30.setText('please add a valid password twice')
    
    
    
    def Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor()

        username = self.lineEdit_20.text()
        password = self.lineEdit_19.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_3.setEnabled(True)

                self.lineEdit_22.setText(row[1])
                self.lineEdit_24.setText(row[2])
                self.lineEdit_21.setText(row[3])
            else : 
                QMessageBox.warning(self , 'Error' , "Make sure your username or password is correct")
                
                
    
    def Edit_User(self):

        username = self.lineEdit_22.text()
        email = self.lineEdit_24.text()
        password = self.lineEdit_21.text()
        password2 = self.lineEdit_23.text()

        original_name = self.lineEdit_20.text()

        if password == password2 :
            self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='bibliotheque')
            self.cur = self.db.cursor()

            

            self.cur.execute('''
                UPDATE users SET user_name=%s , user_email=%s , user_password=%s WHERE user_name=%s
            ''', (username , email , password , original_name))

            self.db.commit()
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            print('make sure you entered you password correctly')
     
    """------- Settings ------- """
     
    
    
      
            
                
    def Add_Category(self):
        
        
        
        
        
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor() 
        
        category_name = self.lineEdit_25.text()
        
        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''' , (category_name,))
        self.db.commit()
        self.statusBar().showMessage('New Category Added ')
        self.lineEdit_25.setText('')
        self.Show_Category()
        
        
    def Show_Category(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category''')
        data = self.cur.fetchall()
        
        if data :
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form) :
                    self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)
    
    
    def Add_Author(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='bibliotheque')
        self.cur = self.db.cursor()
        
        author_name = self.lineEdit_26.text()
        
        self.cur.execute('''
            INSERT INTO author (author_name) VALUES (%s)
        ''' , (author_name,))
        self.db.commit()
        self.statusBar().showMessage('New Author Added ')
        self.lineEdit_26.setText('')
        self.Show_Author()

    def Show_Author(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='bibliotheque')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM author''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)
    
    
    
    """ ------ Show_in_setting --------"""
    
    
    def Show_Category_Combobox(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='bibliotheque')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()

        for category in data :
            self.comboBox_6.addItem(category[0])



    def Show_Author_Combobox(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='bibliotheque')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM author''')
        data = self.cur.fetchall()

        for author in data :
            self.comboBox_7.addItem(author[0])

    




def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
 
 
    