class User(object):
    def __init__(self, firstname=None, lastname=None, email=None, paid_until=None):
        pass
        # Set attributes for firstname, lastname, email, paid_until.
        # Make all attributes None if no arguments are given.
        # firstname, lastname, email should be string.
        # paid_until should be datetime type.

    def is_logged_in(self):
        pass
        # Return boolean
        # This function could be a boolean attribute. Your choice.

    def is_subscribed(self):
        pass
        # Return boolean
        # Check if the user is subscribed to Script Spinner.
        # if today < paid_until: return True, else retunr False

    def getFullname(self):
        pass
        # Return string
        # Get user fullname.

    def login(self, email, password, remember):
        pass
        # Check if user.dat exist. If not,
        # Access the database and authenticate the user.
        # if email and password are valid, retrieve infromation from database
        # then set all attributes.
        # if remember is True, call _remeber function.
        # if email and password are not valid, raise UserNotFoundException

    def logout(self):
        pass
        # Delete the contents of user.dat

    def _remember(self):
        pass
        # Create user.dat then store user information on user,dat file.
        # Save it as JSON format.

    def _set_session_expire_date(self):
        pass
        # Set session expire date. It should be 30 days ahead from today.

    def _update_last_login(self):
        pass
        # Update Last Login date on the database.
        # This function is less important. Don't spend too much time on this.


if __name__ == '__main__':
    pass
    # Create a user class object with no argument.
    # Create a user class object with arguments.
    # Prtnt users full name.
