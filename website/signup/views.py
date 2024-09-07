from django.shortcuts import render, redirect
from django.http import HttpResponse
import mysql.connector as sql  # type: ignore

# Global variables for form data
First_Name = ''
Last_Name = ''
Email = ''
Password = ''

def register(request):
    global First_Name, Last_Name, Email, Password
    if request.method == 'POST':
        d = request.POST
        First_Name = d.get('First_Name')
        Last_Name = d.get('Last_Name')
        Email = d.get('Email')
        Password = d.get('Password')

        try:
            # Establishing the connection to the database
            m = sql.connect(
                host='localhost',
                user='root',
                password='root',
                database='cosmetic'
            )
            cursor = m.cursor()

            # Check if email already exists
            cursor.execute("SELECT * FROM users WHERE Email=%s", (Email,))
            existing_sign = cursor.fetchone()

            if existing_sign:
                return HttpResponse("Email already exists. Please use a different email.")

            # Insert new user into the database
            c = "INSERT INTO users (First_Name, Last_Name, Email, Password) VALUES (%s, %s, %s, %s)"
            cursor.execute(c, (First_Name, Last_Name, Email, Password))
            m.commit()

            # Close the connection
            cursor.close()
            m.close()

            return render(request, 'product_details.html')

        except sql.Error as e:
            return HttpResponse(f"Error inserting data into database: {e}")

    return render(request, 'signup_page.html')
