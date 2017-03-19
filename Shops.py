"""
Created on 26 Feb 2017

@author: metastable
"""


from enum import Enum


class Languages:
    def __init__(self, name, native_name, iso_693_1_code, iso_693_2_code):
        self.name = name
        self.native_name = native_name
        self.iso_693_1_code = iso_693_1_code
        self.iso_693_2_code = iso_693_2_code

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_native_name(self, native_name):
        self.native_name = native_name

    def get_native_name(self):
        return self.native_name

    def set_iso_693_1_code(self, iso_693_1_code):
        self.iso_693_1_code = iso_693_1_code

    def get_iso_693_1_code(self):
        return self.iso_693_1_code

    def set_iso_693_2_code(self, iso_693_2_code):
        self.iso_693_2_code = iso_693_2_code

    def get_iso_693_2_code(self):
        return self.iso_693_2_code

    def __str__(self):
        return self.get_name() + " (" + self.get_native_name() + ")" + " (" + self.get_iso_693_1_code() + ")" \
               + " (" + self.get_iso_693_2_code() + ")"


class Address:
    pass


class ContactDetails:
    def __init__(self, contact_type, organisation_type, name):
        self.contact_type = contact_type
        self.organisation_type = organisation_type
        self.name = name

    def set_contact_type(self, contact_type):
        self.contact_type = contact_type

    def get_contact_type(self):
        return self.contact_type

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.get_contact_type() + " (" + self.get_contact_type() + ")" + " (" + self.get_name() + ")"


class Organisation:
    def __init__(self, organisation, name):
        self.organisation_type = organisation
        self.name = name

    def set_organisation_type(self, organisation):
        self.organisation_type = organisation

    def get_organisation_type(self):
        return self.organisation_type

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.get_name() + " (" + self.get_organisation_type() + ")"


class OrganisationType(Enum):
    COMPANY = 1
    GOVERNMENT = 2
    INSTITUTION = 3
    NON_PROFIT = 4

    def parse_type(self, organisation_type):
        if str(organisation_type).lower == "company":
            return self.COMPANY
        elif str(organisation_type).lower() == "government":
            return self.GOVERNMENT
        elif str(organisation_type).lower() == "institution":
            return self.INSTITUTION
        elif str(organisation_type).lower() == "non_profit":
            return self.NON_PROFIT
        else:
            """ throw an error """
            pass

    def __str__(self):
        return self.name()


class People:
    def __init__(self, first_name, middle_name, last_name, gender, birth_date):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date

    def set_first_name(self, first_name):
        self.self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def get_middle_name(self):
        return self.middle_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def get_birth_date(self):
        return self.birth_date

    def __str__(self):
        return self.get_first_name() + " (" + self.get_middle_name() + "(" + self.get_last_name() + "(" + self.get_gender() + " (" + self.get_birth_date() + ")"


# Table Organisations_Addresses
# Table People_Contact_Details
# Table People_Addresses
# Table People_Languages


class User: # Unique Key
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def __str__(self):
        return self.get_username() + " (" + self.get_password() + ")"


class Shop: # Foreign key
    def __init__(self, name, user):
         self.name = name
         self.user = user

    def set_name(self, name):
         self.name = name

    def get_name(self):
         return self.name

    def set_user(self, user):
         self.user = user

    def get_user(self):
         return self.user

    def __str__(self):
        return self.get_name() + " (" + self.get_user() + ")"

# Table Shops_i18n


class Product:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.set_name = name

    def get_name(self):
        return self.get_name()

    def __str__(self):
        return self.get_name()

# Table Products_i18n


class

