from sqlalchemy import false, true
from src.db_connector import DB_Connector

database = DB_Connector()

class UserController(): 

    def create_user(self, first_name, last_name, isStudent, contact_email, net_id, gender, student_year, password): 
        
        '''
        if isStudent == 'Student':
            isStudent = True
        else:
            isStudent = False
        '''
        
        if gender == 'Male':
            gender = 'M'
        elif gender == 'Female':
            gender = 'F'
        else:
            gender = 'NA'

        database.insert_user(first_name, last_name, isStudent, contact_email, net_id, gender, student_year, password)

    def get_all_users(self):
        users = database.select_all_tickets()
        return users


    def get_user_info_with_matching_email(self, contact_email):
        user_info = database.select_user_with_matching_email(contact_email)
        return user_info

    def get_user_info_with_matching_netid(self, net_id):
        user_info = database.select_user_with_matching_netid(net_id)
        return user_info

    def get_password_with_matching_email(self, contact_email):
        password = database.select_password_with_matching_email(contact_email)
        return password
        

    def get_password_with_matching_netid(self, net_id):
        password = database.select_password_with_matching_netid(net_id)
        return password


    def get_first_name_with_matching_email(self, contact_email):
        first_name = database.select_first_name_with_matching_email(contact_email)
        return first_name

    def get_first_name_with_matching_netid(self, net_id):
        first_name = database.select_first_name_with_matching_netid(net_id)
        return first_name

    def get_last_name_with_matching_email(contact_email):
        last_name = database.select_last_name_with_matching_email(contact_email)
        return last_name

    def get_last_name_with_matching_netid(self, net_id):
        last_name = database.select_last_name_with_matching_netid(net_id)
        return last_name

    def get_firstLast_name_with_matching_email(self, contact_email):
        first_name = self.get_first_name_with_matching_email(contact_email)
        last_name = self.get_last_name_with_matching_email(contact_email)
        name = first_name + " " + last_name
        return name

    def get_firstLast_name_with_matching_netid(self, net_id):
        first_name = self.get_first_name_with_matching_netid(net_id)
        last_name = self.get_last_name_with_matching_netid(net_id)
        name = first_name + " " + last_name
        return name

    def check_user_with_email_exist(self, contact_email):
        #will check if a user with given email already exists in the db
        #if user exists, return true
        #else return false
        user = database.select_user_with_matching_email(contact_email)
        if user:
            return true
        else:
            return false

    def check_user_with_netid_exist(self, net_id):
        #will check if a user with given netid already exists in the db
        #if user exists, return true
        #else return false
        user = database.select_user_with_matching_netid(net_id)
        if user:
            return true
        else:
            return false
            
