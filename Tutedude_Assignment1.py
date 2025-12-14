{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4efde034-3239-4331-bc4d-47fcc3f372c7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "9e0f9a96-3a15-4fbd-8a76-c50657f27caf",
   "metadata": {},
   "source": [
    "# Step 1 - Plan the Data Storage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "39b2d136-e974-4f76-a412-f3ea1c6a8acd",
   "metadata": {},
   "outputs": [],
   "source": [
    "employees = {\n",
    "    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},\n",
    "    102: {'name': 'Rekha', 'age': 30, 'department': 'Finance', 'salary': 60000}\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32820dbb-e4fc-4b35-829e-a5425195c742",
   "metadata": {},
   "source": [
    "# Step 2 - Define the Menu System"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "caf56789-4036-4173-ae97-f43ecdea34ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Employee Management System\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  101\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid choice. Please try again.\n",
      "\n",
      "Employee Management System\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  102\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid choice. Please try again.\n",
      "\n",
      "Employee Management System\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Add Employee selected\n",
      "\n",
      "Employee Management System\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "View All Employees selected\n",
      "\n",
      "Employee Management System\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Search for Employee selected\n",
      "\n",
      "Employee Management System\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting the system\n"
     ]
    }
   ],
   "source": [
    "employees = {\n",
    "    101: {\n",
    "        \"name\": \"Satya\",\n",
    "        \"age\": 27,\n",
    "        \"department\": \"HR\",\n",
    "        \"salary\": 50000\n",
    "    }\n",
    "}\n",
    "\n",
    "def add_employee(employees):\n",
    "    emp_id = int(input(\"Enter Employee ID: \"))\n",
    "    name = input(\"Enter Employee Name: \")\n",
    "    age = int(input(\"Enter Employee Age: \"))\n",
    "    department = input(\"Enter Department: \")\n",
    "    salary = int(input(\"Enter Salary: \"))\n",
    "\n",
    "    employees[emp_id] = {\n",
    "        \"name\": name,\n",
    "        \"age\": age,\n",
    "        \"department\": department,\n",
    "        \"salary\": salary\n",
    "    }\n",
    "\n",
    "    print(\"Employee added successfully!\")\n",
    "\n",
    "while True:\n",
    "    print(\"\\nEmployee Management System\")\n",
    "    print(\"1. Add Employee\")\n",
    "    print(\"2. View All Employees\")\n",
    "    print(\"3. Search for Employee\")\n",
    "    print(\"4. Exit\")\n",
    "\n",
    "    choice = input(\"Enter your choice: \")\n",
    "\n",
    "    if choice == \"1\":\n",
    "        add_employee(employees)\n",
    "\n",
    "    elif choice == \"4\":\n",
    "        print(\"Exiting...\")\n",
    "        break\n",
    "\n",
    "    else:\n",
    "        print(\"Option will be added later\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "058d9c89-6cef-47fb-b5cc-0ebebc8bafd0",
   "metadata": {},
   "source": [
    "# Step 3 - Add Employee Functionality"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "71e0ae87-072c-4d36-ac14-b34e2145ff13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Add employee function called.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Employee ID:  103\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This Employee ID already exists. Please enter a different ID.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Employee ID:  104\n",
      "Enter Employee Name:  Gopal\n",
      "Enter Employee Age:  31\n",
      "Enter Employee Department:  IT\n",
      "Enter Employee Salary:  80000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee with ID 104 added successfully.\n"
     ]
    }
   ],
   "source": [
    "employees = {\n",
    "    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},\n",
    "    102: {'name': 'Rekha', 'age': 30, 'department': 'Finance', 'salary': 60000}\n",
    "}  \n",
    "\n",
    "def add_employee():\n",
    "    print(\"Add employee function called.\")\n",
    "\n",
    "    while True:\n",
    "        try:\n",
    "            emp_id = int(input(\"Enter Employee ID: \"))\n",
    "            if emp_id in employee_data:\n",
    "                print(\"This Employee ID already exists. Please enter a different ID.\")\n",
    "            else:\n",
    "                break\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Employee ID should be an integer.\")\n",
    "\n",
    "    name = input(\"Enter Employee Name: \")\n",
    "\n",
    "    while True:\n",
    "        try:\n",
    "            age = int(input(\"Enter Employee Age: \"))\n",
    "            break\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Age should be an integer.\")\n",
    "\n",
    "    department = input(\"Enter Employee Department: \")\n",
    "\n",
    "    while True:\n",
    "        try:\n",
    "            salary = float(input(\"Enter Employee Salary: \"))\n",
    "            break\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Salary should be a number.\")\n",
    "\n",
    "    employee_data[emp_id] = {\n",
    "        'name': name,\n",
    "        'age': age,\n",
    "        'department': department,\n",
    "        'salary': salary\n",
    "    }\n",
    "\n",
    "    print(f\"Employee with ID {emp_id} added successfully.\")\n",
    "\n",
    "\n",
    "add_employee()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ced64ba4-b719-4e6c-83a2-9441c111b5e1",
   "metadata": {},
   "source": [
    "# Step 4 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "9e7d6e19-6d70-4684-a970-57fa681485da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "ID\tName\tAge\tDepartment\tSalary\n",
      "--------------------------------------------------\n",
      "101 \t Satya \t 27 \t HR \t 50000\n",
      "102 \t Amit \t 30 \t IT \t 60000\n",
      "104 \t Gopal \t 31 \t IT \t 80000\n"
     ]
    }
   ],
   "source": [
    "employees = {\n",
    "    101: {\"name\": \"Satya\", \"age\": 27, \"department\": \"HR\", \"salary\": 50000},\n",
    "    \n",
    "    102: {\"name\": \"Amit\", \"age\": 30, \"department\": \"IT\", \"salary\": 60000},\n",
    "\n",
    "    104: {\"name\": \"Gopal\", \"age\": 31, \"department\": \"IT\", \"salary\": 80000}\n",
    "    \n",
    "   }\n",
    "\n",
    "def view_all_employees(employees):\n",
    "    if not employees:\n",
    "        print(\"No employees available.\")\n",
    "        return\n",
    "\n",
    "    print(\"\\nID\\tName\\tAge\\tDepartment\\tSalary\")\n",
    "    print(\"-\" * 50)\n",
    "\n",
    "    for emp_id, details in employees.items():\n",
    "        print(emp_id, \"\\t\",\n",
    "              details[\"name\"], \"\\t\",\n",
    "              details[\"age\"], \"\\t\",\n",
    "              details[\"department\"], \"\\t\",\n",
    "              details[\"salary\"])\n",
    "\n",
    "\n",
    "view_all_employees(employees)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90239d74-3925-44ae-b192-c9866923edee",
   "metadata": {},
   "source": [
    "# Step 5 - Search for an Employee by ID"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "46cb7b31-202c-487f-9f83-1044ad6037d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Employee ID to search:  104\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Employee Found\n",
      "Name: Gopal\n",
      "Age: 31\n",
      "Department: IT\n",
      "Salary: 80000\n"
     ]
    }
   ],
   "source": [
    "employees = {\n",
    "    101: {\"name\": \"Satya\", \"age\": 27, \"department\": \"HR\", \"salary\": 50000},\n",
    "    102: {\"name\": \"Rekha\", \"age\": 30, \"department\": \"IT\", \"salary\": 60000},\n",
    "    104: {\"name\": \"Gopal\", \"age\": 31, \"department\": \"IT\", \"salary\": 80000}\n",
    "}\n",
    "\n",
    "def search_employee(employees):\n",
    "    emp_id = int(input(\"Enter Employee ID to search: \"))\n",
    "\n",
    "    if emp_id in employees:\n",
    "        details = employees[emp_id]\n",
    "        print(\"\\nEmployee Found\")\n",
    "        print(\"Name:\", details[\"name\"])\n",
    "        print(\"Age:\", details[\"age\"])\n",
    "        print(\"Department:\", details[\"department\"])\n",
    "        print(\"Salary:\", details[\"salary\"])\n",
    "    else:\n",
    "        print(\"Employee not found.\")\n",
    "\n",
    "search_employee(employees)   # 👈 FUNCTION CALL\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2baa8fbd-1776-438c-9331-21f86c66660f",
   "metadata": {},
   "source": [
    "# Step 6 - Exit the Program"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "b0d96b83-71cf-4992-95dd-a9b811766922",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for using the Employee Management System!\n"
     ]
    }
   ],
   "source": [
    "\n",
    "if choice == \"1\":\n",
    "    # Code for option 1\n",
    "    pass\n",
    "elif choice == \"2\":\n",
    "    # Code for option 2\n",
    "    pass\n",
    "elif choice == \"3\":\n",
    "    # Code for option 3\n",
    "    pass\n",
    "elif choice == \"4\":\n",
    "    print(\"Thank you for using the Employee Management System!\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
