import sys
from subprocess import run
import os

WIDTH = 40


def print_menu():

	pretty_print()
	pretty_print("[1] List environments", delimiter="|")
	pretty_print("[2] List packages", delimiter="|")
	pretty_print("[3] Create new environment", delimiter="|")
	pretty_print("[4] Remove environment", delimiter="|")
	pretty_print("[5] Clone environment", delimiter="|")
	pretty_print("[6] Exit", delimiter="|")
	pretty_print()



def pretty_print(text: str = None, delimiter: str = ""):

	if not text:
		for i in range(WIDTH):
			print("-", end=delimiter)
		print()

	else:
		print(delimiter + " " + text, end="")
		for i in range(WIDTH - len(text) - 3):
			print(" ", end="")
		print(delimiter)



def select_environment(msg):

	output = run(["conda", "info", "--envs"], capture_output=True).stdout.decode("utf-8") 
	envs = output.split("\n")[2:-2]
	envs = [env.split(" ")[0] for env in envs]
	idx = 1

	for env in envs:
		pretty_print(f"{idx}. {env}", delimiter="")
		idx += 1

	# Ask for a valid number
	selected_idx = None;
	while not selected_idx:
		try:
			selected_idx = int(input(msg)) - 1
		except:
			print("Please enter a valid number")

	return (envs[selected_idx])


def main():
	print_menu()
	user_input = input("Your choice: ")

	while user_input != "6":

		# List environments
		if (user_input == "1"):
			run(["conda", "info", "--envs"])

		# List packages
		elif (user_input == "2"):
			run(["conda", "list"])

		# Create new environment
		elif (user_input == "3"):
			env_name = "_".join(input("Name of the environment to be created: ").split(" "))
			python_ver = input("Python version (default is 3.9.5): ")
			python_ver = "3.9.5" if (python_ver == "") else python_ver
			run(["conda", "create", "-n", env_name, f"python={python_ver}", "-y"])

		# Remove environment
		elif (user_input == "4"):
			env_name = select_environment("Environment to be removed: ")
			# run(["conda", "deactivate"])
			run(["conda", "activate", "bash"])
			run(["conda", "remove", "-n", env_name, "--all", "-y"])

		# Clone environment
		elif (user_input == "5"):
			env_name = select_environment("Environment to be cloned: ")
			new_name = "_".join(input("Name of the cloned environment: ").split(" "))
			run(["conda", "create", "-n", new_name, "--clone", env_name])

		print_menu()
		user_input = input("Your choice: ")


if __name__ == "__main__":
	main()
