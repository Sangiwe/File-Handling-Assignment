with open("my_file.txt" , "w") as file:
  file.write("Hey my name is Luke.\n")
  file.write("I am 25 years old.\n")
  file.write("Residing in Durban.\n")

with open("my_file.txt" , "a") as file:
  file.write("Hey my name is Daisy.\n")
  file.write("I am 23 years old.\n")
  file.write("Residing in Port Elizabeth.\n")

with open("my_file.txt", "r") as file:
    content = file.read()  
    print("File Contents:\n")
    print(content)  

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("File operations complete.")