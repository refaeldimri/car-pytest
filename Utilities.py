import os
from datetime import datetime
import dotenv
dotenv.load_dotenv()


class Utilities:
    file = None

    def writeToFile(self, string):
        dotenv.load_dotenv()
        """
        This function get a string and write it to self.file.
        :param string:
        :return None:
        """
        os.chdir(os.getcwd())
        try:
            self.file = open(os.getenv("FILENAME"), "a")
            string += datetime.now().strftime(", " + os.getenv("TIMESTAMP") + "\n")
            self.file.write(string)
            self.file.flush()
            self.file.close()
        except Exception as e:
            self.writeToFile(os.getenv("FILE_ERROR") + str(e))
