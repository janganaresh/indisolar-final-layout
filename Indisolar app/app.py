from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import mysql.connector


app = Flask(__name__)
app.secret_key = 'your_secret_key' 

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nari@2058",  
        database="remedydb"
    )

# Route to render the login.html page
@app.route('/')
def index():
    return render_template('login.html')

# Route for the home page
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')  # Redirect to login if not authenticated

    user_type = session.get('user_type', 'Normal User')
    username = session.get('username')  # Get the username from the session
    return render_template('dashboard.html', user_type=user_type, username=username)

# for create route 
@app.route('/site')
def site():
    return render_template('site.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/userform')
def userform():
    return render_template('userform.html')

@app.route('/area')
def area():
    return render_template('area.html')

@app.route('/rows')
def rows():
    return render_template('rows.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/piles')
def piles():
    return render_template('pile.html')

@app.route('/assessment')
def assessment():
    return render_template('assessment.html')

@app.route('/remedy')
def remedy():
    return render_template('remedy.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/invtrans')
def invtrans():
    return render_template('invtrans.html')

@app.route('/quality')
def quality():
    return render_template('quality.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/profile', methods=['GET'])
def profile():
    if 'username' not in session:
        return redirect('/login')  # Redirect if not logged in

    username = session['username']
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Fetch the user's data from the 'users' table
    cursor.execute("SELECT * FROM users WHERE `User Name` = %s", (username,))
    user = cursor.fetchone()

    if not user:
        return redirect('/login')  # Redirect if user not found

    # Pass only the user data to the profile template
    return render_template('profile.html', user=user)

@app.route('/user_log')
def user_log():
    return render_template('user_log.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

################################################################

#for update route

@app.route('/updateusers')
def update_users():
    # Render the page where you handle user update
    return render_template('updateusers.html')

@app.route('/updatesite')
def update_site():
    # Render the page where you handle user update
    return render_template('updatesite.html')

@app.route('/updatecustomer')
def update_customer():
    # Render the page where you handle user update
    return render_template('updatecustomer.html')

@app.route('/updateinventory')
def update_inventory():
    # Render the page where you handle user update
    return render_template('updateinventory.html')

@app.route('/updateinvtrans')
def update_invtrans():
    # Render the page where you handle user update
    return render_template('updateinvtrans.html')

@app.route('/updatearea')
def update_area():
    return render_template('updatearea.html')

@app.route('/updatetable')
def update_table():
    return render_template('updatetable.html')

@app.route('/updatepile')
def update_pile():
    return render_template('updatepile.html')

@app.route('/updaterow')
def update_row():
    return render_template('updaterow.html')

@app.route('/updateassmnt')
def update_assmnt():
    return render_template('updateassmnt.html')

@app.route('/updateremedy')
def update_remedy():
    return render_template('updateremedy.html')

###########################################################

# Route for user login verification
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    if user:
        session['username'] = user['User Name'] 
        session['user_type'] = user['User Type'] # Store the usertype in the session
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"})

# Route for user creation
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO loginusers (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, password))
        connection.commit()
        return jsonify({"success": True, "message": "User created successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error creating user: {e}"})

# Route for logging out
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect(url_for('index'))

@app.route('/submit_siteform', methods=['POST'])
def submit_siteform():
    site_name = request.form.get('site_name')
    site_location = request.form.get('location')
    site_owner = request.form.get('site_owner_name')
    site_gps = request.form.get('site_gps')

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the current maximum Site ID
        cursor.execute("SELECT `Site ID` FROM `Site` ORDER BY `Site ID` DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
            # Extract the numeric part of the Site ID and increment it
            last_site_id = result[0]  # Example: 'S005'
            next_number = int(last_site_id[1:]) + 1  # Extract '005' and add 1
        else:
            # No entries exist; start from 1
            next_number = 1

        # Generate the new Site ID
        new_site_id = f"S{next_number:03d}"  # Format as 'S001', 'S002', etc.

        # Insert the new row with the generated Site ID
        query = """
        INSERT INTO `Site` (`Site ID`, `Cust ID`, `Site Name`, `Site Location`, `Site Owner Name`, `Site GPS`)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_site_id, "", site_name, site_location, site_owner, site_gps))
        connection.commit()

        return jsonify({"success": True, "message": f"Site information saved successfully with ID {new_site_id}"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving site information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_customerform', methods=['POST'])
def submit_customerform():
    # Getting data from the form
    name = request.form.get('name')
    address = request.form.get('address')
    contact_person = request.form.get('contact_person')
    website = request.form.get('website')
    phone_no = request.form.get('phone_no')
    country = request.form.get('country')

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch the current maximum Cust ID
        cursor.execute("SELECT `Cust ID` FROM `Customer` ORDER BY `Cust ID` DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
            # Extract the numeric part of the Cust ID and increment it
            last_cust_id = result[0]  # Example: 'C005'
            next_number = int(last_cust_id[1:]) + 1  # Extract '005' and add 1
        else:
            # No entries exist; start from 1
            next_number = 1

        # Generate the new Cust ID
        new_cust_id = f"C{next_number:03d}"  # Format as 'C001', 'C002', etc.

        # Insert the new row with the generated Cust ID
        query = """
        INSERT INTO Customer 
        (`Cust ID`, `Customer Name`, `Customer Address`, `Contact Person`, `Customer Website`, `Phone No`, `Country`)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_cust_id, name, address, contact_person, website, phone_no, country))
        connection.commit()

        return jsonify({"success": True, "message": f"Customer information saved successfully with ID {new_cust_id}"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving customer information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_user_form', methods=['POST'])
def submit_userform():
    # Retrieve form data
    user_name = request.form.get('user_name')
    user_type = request.form.get('user_type')
    designation = request.form.get('designation')
    phone_no = request.form.get('phone_no')
    reports_to = request.form.get('reports_to')
    date_created = request.form.get('date_created')
    site_id = request.form.get('site_id')  # Get the selected Site ID
    email = request.form.get('gmail_address')  # Get email from the form
    password = request.form.get('create_password')  # Get password from the form

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Check if the Site ID exists
        cursor.execute("SELECT `Site ID` FROM `site` WHERE `Site ID` = %s", (site_id,))
        if not cursor.fetchone():
            return jsonify({"success": False, "message": "Invalid Site ID selected."})

        # Check if the email already exists in the database
        cursor.execute("SELECT `Email` FROM `users` WHERE `Email` = %s", (email,))
        if cursor.fetchone():
            return jsonify({"success": False, "message": "Email already exists. Please use a different email."})

        # Fetch the current maximum User ID
        cursor.execute("SELECT `User ID` FROM `users` ORDER BY `User ID` DESC LIMIT 1")
        result = cursor.fetchone()
        if result and result[0]:
            last_user_id = result[0]
            next_number = int(last_user_id[1:]) + 1
        else:
            next_number = 1

        new_user_id = f"U{next_number:03d}"  # Format as 'U001', 'U002', etc.

        # Insert data into the users table
        query = """
        INSERT INTO `users` (`User ID`, `Site ID`, `User Name`, `User Type`, `User Designation`, `User Phone number`, `Reports To`, `Date Created`, `Date Removed`, `Email`, `Password`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_user_id, site_id, user_name, user_type, designation, phone_no, reports_to, date_created, None, email, password))
        connection.commit()

        return jsonify({"success": True, "message": f"User information saved successfully with ID {new_user_id}"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving user information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_area_form', methods=['POST'])
def submit_area_form():
    # Retrieve form data
    location = request.form.get('location')
    gps = request.form.get('gps')

    # Validate if required fields are provided
    if not location or not gps:
        return jsonify({"success": False, "message": "All fields are required."})

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the current maximum Area ID
        cursor.execute("SELECT `Area ID` FROM `areas` ORDER BY `Area ID` DESC LIMIT 1")
        result = cursor.fetchone()
        
        # Determine the next Area ID
        if result and result[0]:
            last_area_id = result[0]
            next_number = int(last_area_id[1:]) + 1
        else:
            next_number = 1

        # Format the new Area ID as 'A001', 'A002', etc.
        new_area_id = f"A{next_number:03d}"

        # Insert data into the areas table with the generated Area ID
        query = """
        INSERT INTO `areas` (`Area ID`, `Location`, `GPS`)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (new_area_id, location, gps))  # Set `Area ID` as generated
        connection.commit()

        return jsonify({"success": True, "message": f"Area information saved successfully with ID {new_area_id}"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving area information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_user_log_form', methods=['POST'])
def submit_user_log_form():
    # Retrieve form data
    user_id = request.form.get('user_id')
    date_logged_in = request.form.get('date_logged_in')
    date_logged_out = request.form.get('date_logged_out')

    # Validate if required fields are provided
    if not user_id or not date_logged_in:
        return jsonify({"success": False, "message": "User ID and Date Logged In are required."})

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Insert data into the users_log table
        query = """
        INSERT INTO `user_log` (`User ID`, `Date Logged in`, `Date Logged out`)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (user_id, date_logged_in, date_logged_out))
        connection.commit()
        return jsonify({"success": True, "message": "User log information saved successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving user log information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_comment_form', methods=['POST'])
def submit_comment_form():
    comment_type = request.form.get('comment_type')
    related_comment_id = request.form.get('related_comment_id')
    pile_id = request.form.get('pile_id')
    user_id = request.form.get('user_id')
    usage_id = request.form.get('usage_id')
    date_posted = request.form.get('date_posted')
    comment_text = request.form.get('comment_text')
    comment_date = request.form.get('comment_date')
    commented_by = request.form.get('commented_by')
    status = request.form.get('status')

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Insert the data into the Comment table
        query = """
        INSERT INTO `Comments` (`Comment Type`, `Related Comment ID`, `Pile ID`, `User ID`, `Usage ID`, 
                               `Date Posted`, `Comment Text`, `Comment Date`, `Commented By`, `Status`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (comment_type, related_comment_id, pile_id, user_id, usage_id,
                               date_posted, comment_text, comment_date, commented_by, status))
        connection.commit()
        return jsonify({"success": True, "message": "Comment information saved successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving comment information: {e}"})
    finally:
        cursor.close()
        connection.close()

#connection for assessment
@app.route('/submit_task_assignment', methods=['POST'])
def submit_task_assignment():
    # Get the form data from the request
    user_id = request.form.get('user_id')
    pile_id = request.form.get('pile_id')
    task_date = request.form.get('task_date')
    allotted_date = request.form.get('allotted_date')
    allotted_by = request.form.get('allotted_by')
    date_completed = request.form.get('date_completed')
    assessment_status = request.form.get('assessment_status')
    assessment_case = request.form.get('assessment_case')
    picture_name = request.form.get('picture_name')
    picture_location = request.form.get('picture_location')

    # Establish a database connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Insert the data into the Task Assignment table
        query = """
        INSERT INTO `assessment` (`User ID`, `Pile ID`, `Task Date`, `Allotted Date`, `Allotted By`, `Date Completed`, 
                                       `Assessment Status`, `Assessment Case`, `Picture Name`, `Picture Location`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, pile_id, task_date, allotted_date, allotted_by, date_completed, 
                               assessment_status, assessment_case, picture_name, picture_location))
        connection.commit()
        
        return jsonify({"success": True, "message": "Task assignment saved successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving task assignment: {e}"})

@app.route('/submit_row_form', methods=['POST'])
def submit_row_form():
    # Retrieve form data
    row_name = request.form.get('row_name')
    area_id = request.form.get('area_id')
    location = request.form.get('location')
    gps = request.form.get('gps')

    # Validate required fields
    if not row_name or not area_id or not location or not gps:
        return jsonify({"success": False, "message": "All fields are required."})

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the current maximum Row ID
        cursor.execute("SELECT `Row ID` FROM `rows` ORDER BY `Row ID` DESC LIMIT 1")
        result = cursor.fetchone()

        # Determine the next Row ID
        if result and result[0]:
            last_row_id = result[0]
            next_number = int(last_row_id[1:]) + 1
        else:
            next_number = 1

        # Format the new Row ID as 'R001', 'R002', etc.
        new_row_id = f"R{next_number:03d}"

        # Insert data into the rows table with the generated Row ID
        query = """
        INSERT INTO `rows` (`Row ID`, `Row Name`, `Area ID`, `Location`, `GPS`)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_row_id, row_name, area_id, location, gps))
        connection.commit()

        return jsonify({"success": True, "message": f"Row information saved successfully with ID {new_row_id}"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving row information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_pile_form', methods=['POST'])
def submit_pile_form():
    # Get form data
    table_id = request.form.get('table_id')
    row_id = request.form.get('row_id')
    area_id = request.form.get('area_id')
    location_description = request.form.get('location_description')
    gps_location = request.form.get('gps_location')

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the current maximum pile_id
        cursor.execute("SELECT `Pile ID` FROM `Piles` ORDER BY `Pile ID` DESC LIMIT 1")
        result = cursor.fetchone()

        # Generate the next Pile ID
        if result and result[0]:
            last_pile_id = result[0]
            next_number = int(last_pile_id[1:]) + 1  # Extract numeric part, increment it
        else:
            next_number = 1  # If no rows, start with P001

        # Format the new Pile ID as 'P001', 'P002', etc.
        new_pile_id = f"P{next_number:03d}"

        # Insert data into Pile Form table
        query = """
        INSERT INTO `Piles` (`Pile ID`, `Table ID`, `Row ID`, `Area ID`, `Location Description`, `GPS Location`)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_pile_id, table_id, row_id, area_id, location_description, gps_location))
        connection.commit()

        print("Data inserted successfully")
        return jsonify({"success": True, "message": "Pile information saved successfully"})

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": f"Error saving pile information: {e}"})

    finally:
        cursor.close()
        connection.close()

@app.route('/submit_table_form', methods=['POST'])
def submit_table_form():
    # Retrieve form data
    row_id = request.form.get('row_id')
    area_id = request.form.get('area_id')
    location = request.form.get('location')
    gps = request.form.get('gps')

    # Validate required fields
    if not row_id or not area_id or not location:
        return jsonify({"success": False, "message": "Row ID, Area ID, and Location are required."})

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the current maximum Table ID
        cursor.execute("SELECT `Table ID` FROM `Tables` ORDER BY `Table ID` DESC LIMIT 1")
        result = cursor.fetchone()
        
        # Determine the next Table ID
        if result and result[0]:
            last_table_id = result[0]
            next_number = int(last_table_id[1:]) + 1
        else:
            next_number = 1

        # Format the new Table ID as 'T001', 'T002', etc.
        new_table_id = f"T{next_number:03d}"

        # Insert data into the Tables table with the generated Table ID
        query = """
        INSERT INTO `Tables` (`Table ID`, `Row ID`, `Area ID`, `Location`, `GPS`)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_table_id, row_id, area_id, location, gps))
        connection.commit()

        return jsonify({"success": True, "message": f"Table information saved successfully with ID {new_table_id}"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving table information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_remedy_form', methods=['POST'])
def submit_remedy_form():
    # Get form data
    user_id = request.form.get('user_id')
    pile_id = request.form.get('pile_id')
    task_date = request.form.get('task_date')
    assessed_case = request.form.get('assessed_case')
    allotted_date = request.form.get('allotted_date')
    allotted_by = request.form.get('allotted_by')
    date_completed = request.form.get('date_completed')
    remedy_status = request.form.get('remedy_status')
    remedy_text = request.form.get('remedy_text')
    picture_name = request.form.get('picture_name')
    picture_location = request.form.get('picture_location')

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Insert data into Remedy Form table
        query = """
        INSERT INTO `Remedy` (`User ID`, `Pile ID`, `Task Date`, `Assessed Case`, 
                                  `Allotted Date`, `Allotted By`, `Date Completed`, 
                                  `Remedy Status`, `Remedy Text`, `Picture Name`, `Picture Location`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, pile_id, task_date, assessed_case, allotted_date, 
                               allotted_by, date_completed, remedy_status, remedy_text, 
                               picture_name, picture_location))
        connection.commit()

        print("Data inserted successfully")
        return jsonify({"success": True, "message": "User task information saved successfully"})

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": f"Error saving user task information: {e}"})

@app.route('/submit_inventory_details', methods=['POST'])
def submit_inventory_details():
    # Get form data
    item_type = request.form.get('item_type')
    item_uom = request.form.get('item_uom')
    item_desc = request.form.get('item_desc')
    item_avl_qty = request.form.get('item_avl_qty')
    item_ror = request.form.get('item_ror') or None
    item_value = request.form.get('item_value') or None
    item_rate = request.form.get('item_rate') or None

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Generate the next Item ID
        cursor.execute("SELECT `Item ID` FROM `Inventory` ORDER BY `Item ID` DESC LIMIT 1")
        result = cursor.fetchone()
        
        if result and result[0]:
            last_item_id = result[0]
            next_number = int(last_item_id[1:]) + 1
        else:
            next_number = 1
        
        # Format the new Item ID as 'I001', 'I002', etc.
        new_item_id = f"I{next_number:03d}"

        # Insert data into Inventory table
        query = """
        INSERT INTO `Inventory` (`Item ID`, `Item Type`, `Item UOM`, `Item Desc`, 
                                 `Item Avl Qty`, `Item ROR`, `Item Value`, `Item Rate`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_item_id, item_type, item_uom, item_desc, item_avl_qty, item_ror, item_value, item_rate))
        connection.commit()

        print(f"Data inserted successfully with Item ID: {new_item_id}")
        return jsonify({"success": True, "message": f"Item details saved successfully with Item ID: {new_item_id}"})

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": f"Error saving item details: {e}"})

    finally:
        cursor.close()
        connection.close()

#invtrans
@app.route('/submit_item_transaction_form', methods=['POST'])
def submit_item_transaction_form():
    # Get form data
  
    trans_qty = request.form.get('trans_qty')
    trans_type = request.form.get('trans_type')
    trans_date = request.form.get('trans_date')
    user_id = request.form.get('user_id')
    usage = request.form.get('usage')

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Generate the next Item ID
        cursor.execute("SELECT `Item ID` FROM `Invtrans` ORDER BY `Item ID` DESC LIMIT 1")
        result = cursor.fetchone()
        
        if result and result[0]:
            last_item_id = result[0]
            next_number = int(last_item_id[1:]) + 1
        else:
            next_number = 1
        
        # Format the new Item ID as 'I001', 'I002', etc.
        new_item_id = f"IT{next_number:03d}"
        # Insert data into Item Transaction table
        query = """
        INSERT INTO `invtrans` (`Item ID`, `Trans Qty`, `Trans Type`, 
                                       `Trans Date`, `User ID`, `Usage`)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_item_id, trans_qty, trans_type, trans_date, user_id, usage))
        connection.commit()

        print("Data inserted successfully")
        return jsonify({"success": True, "message": "Item transaction details saved successfully"})

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": f"Error saving item transaction details: {e}"})

###########################################################################

# select options get
@app.route('/get_user_ids', methods=['GET'])
def get_user_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT `User ID`, `User Name` FROM `users`")
        users = [{"id": row[0], "username": row[1]} for row in cursor.fetchall()]
        return jsonify({"success": True, "users": users})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching User IDs and Usernames: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_site_ids', methods=['GET'])
def get_site_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT `Site ID`, `Site Name` FROM `site`")
        sites = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        return jsonify({"success": True, "sites": sites})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching Site IDs and Site Names: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_area_ids', methods=['GET'])
def get_area_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch Area IDs and Locations
        cursor.execute("SELECT `Area ID`, `Location` FROM `areas`")
        areas = [{"id": row[0], "location": row[1]} for row in cursor.fetchall()]
        return jsonify({"success": True, "areas": areas})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching Area IDs and Locations: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route("/get_row_ids", methods=["GET"])
def get_row_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch Row IDs and Row Names from the database
        cursor.execute("SELECT `Row ID`, `Row Name` FROM `rows`")
        rows = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        return jsonify({"success": True, "rows": rows})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching rows: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route("/get_table_ids", methods=["GET"])
def get_table_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch Table IDs and Locations from the database
        cursor.execute("SELECT `Table ID`, `Location` FROM `tables`")
        tables = [{"id": table[0], "location": table[1]} for table in cursor.fetchall()]
        return jsonify({"success": True, "tables": tables})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching tables: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_customer_ids', methods=['GET'])
def get_customer_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch Customer ID and Customer Name from the database
        cursor.execute("SELECT `Cust ID`, `Customer Name` FROM `customer`")
        customers = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        
        # Return the list of customers as a JSON response
        return jsonify({"success": True, "customers": customers})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching Customer IDs and Names: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_item_names', methods=['GET'])
def get_item_names():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT DISTINCT `Item Type` as item_name FROM inventory")
        items = cursor.fetchall()
        return jsonify({"items": items})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Get the search query from the request
    results = []

    try:
        # Connect to the database using get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # SQL Query to search for assessment names
        sql_query = """
        SELECT `assessment id`
        FROM assessment
        WHERE `assessment id` LIKE %s
        LIMIT 10
        """
        cursor.execute(sql_query, (f"%{query}%",))

        # Fetch all results
        results = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return jsonify({"results": results})

@app.route('/search_by_date', methods=['GET'])
def search_by_date():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # Using dictionary=True for column names in results
    date = request.args.get('date')  # Getting the date from query parameters

    if not date:
        return jsonify({"error": "Date parameter is required"}), 400

    try:
        # Query to fetch assessment_status and assessment_case for the given date
        cursor.execute("""
            SELECT DISTINCT `Assessment Status` as assessment_status, 
                            `Assessment Case` as assessment_case
            FROM assessment 
            WHERE `Task Date` = %s
        """, (date,))
        result = cursor.fetchone()  # Fetch the first matching row
        
        if result:
            return jsonify({
                "assessment_status": result['assessment_status'],
                "assessment_case": result['assessment_case']
            })
        else:
            return jsonify({"error": "No assessments found for the given date"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/search_by_remedydate', methods=['GET'])
def search_by_remedydate():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # Using dictionary=True for column names in results
    date = request.args.get('date')  # Getting the date from query parameters

    if not date:
        return jsonify({"error": "Date parameter is required"}), 400

    try:
        # Query to fetch remedy_status and assessed_case for the given date
        cursor.execute("""
            SELECT DISTINCT `Remedy Status` as remedy_status, 
                            `Assessed Case` as assessed_case
            FROM remedy 
            WHERE `Allotted Date` = %s
        """, (date,))
        result = cursor.fetchone()  # Fetch the first matching row
        
        if result:
            return jsonify({
                "remedy_status": result['remedy_status'],
                "assessed_case": result['assessed_case']
            })
        else:
            return jsonify({"error": "No remedies found for the given date"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()


#############################################################################

@app.route('/submit_updateuser_form', methods=['POST'])
def submit_updateuser_form():
    user_id = request.form.get('user_id')  # User ID is required to identify the user
    user_email = request.form.get('user_email')  # Optional field for email
    user_password = request.form.get('user_password')  # Optional field for password
    phone_no = request.form.get('phone_no')  # Optional field for phone number

    # Connect to the database
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Build the UPDATE query dynamically based on provided fields
        update_fields = []
        params = []

        if user_email:
            update_fields.append("`Email` = %s")
            params.append(user_email)

        if user_password:
            update_fields.append("`Password` = %s")
            params.append(user_password)

        if phone_no:
            update_fields.append("`User Phone number` = %s")
            params.append(phone_no)

        if not update_fields:
            return jsonify({"success": False, "message": "No fields to update provided."})

        params.append(user_id)
        query = f"""
            UPDATE `users`
            SET {', '.join(update_fields)}
            WHERE `User ID` = %s
        """
        cursor.execute(query, tuple(params))
        connection.commit()

        return jsonify({"success": True, "message": "User Details updated successfully."})

    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error updating user: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Check if the user exists
        cursor.execute("SELECT `User ID` FROM `users` WHERE `User ID` = %s", (user_id,))
        if not cursor.fetchone():
            return jsonify({"success": False, "message": "User not found."})

        # Delete the user
        cursor.execute("DELETE FROM `users` WHERE `User ID` = %s", (user_id,))
        connection.commit()

        return jsonify({"success": True, "message": "User deleted successfully."})

    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error deleting user: {e}"})
    finally:
        cursor.close()
        connection.close()

# Update site details
@app.route("/submit_site_update", methods=["POST"])
def submit_site_update():
    try:
        data = request.form
        site_id = data.get("site_id")
        site_location = data.get("location")
        site_owner_name = data.get("site_owner_name")

        if not site_id or not site_location or not site_owner_name:
            return jsonify({"success": False, "message": "All fields are required."})

        connection = get_db_connection()
        cursor = connection.cursor()

        # Enclose column names with spaces in backticks
        query = """
            UPDATE `site` 
            SET `Site Location` = %s, `Site Owner Name` = %s 
            WHERE `Site ID` = %s
        """
        cursor.execute(query, (site_location, site_owner_name, site_id))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Site updated successfully."})
        else:
            return jsonify({"success": False, "message": "No changes made or site not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        cursor.close()
        connection.close()

# Delete a site
@app.route("/delete_site/<site_id>", methods=["DELETE"])
def delete_site(site_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Use backticks for column names
        query = "DELETE FROM `site` WHERE `Site ID` = %s"
        cursor.execute(query, (site_id,))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Site deleted successfully."})
        else:
            return jsonify({"success": False, "message": "Site not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        cursor.close()
        connection.close()

# Route to handle customer update
@app.route('/submit_customer_update', methods=['POST'])
def submit_customer_update():
    try:
        # Get form data
        customer_id = request.form.get('customer_name')
        address = request.form.get('address')
        phone_no = request.form.get('phone_no')

        if not customer_id:
            return jsonify({"success": False, "message": "Customer ID is required."})

        # Initialize list to store the updates
        updates = []
        values = []

        # Only add fields if they are provided
        if address:
            updates.append("`Customer Address` = %s")
            values.append(address)
        if phone_no:
            updates.append("`Phone No` = %s")
            values.append(phone_no)

        # If no updates are provided, return an error
        if not updates:
            return jsonify({"success": False, "message": "At least one field should be provided to update."})

        # Add the customer_id to the end of values
        values.append(customer_id)

        # Create the SQL query dynamically based on provided fields
        query = f"""
            UPDATE `customer`
            SET {', '.join(updates)}
            WHERE `Cust ID` = %s
        """

        # Get database connection
        connection = get_db_connection()
        cursor = connection.cursor()

        # Execute the update query
        cursor.execute(query, tuple(values))
        connection.commit()

        # Check if the update was successful
        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Customer updated successfully."})
        else:
            return jsonify({"success": False, "message": "No changes made or customer not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Route to handle customer deletion
@app.route("/delete_customer/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Delete query with backticks for columns
        query = "DELETE FROM `customer` WHERE `Cust ID` = %s"
        cursor.execute(query, (customer_id,))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Customer deleted successfully."})
        else:
            return jsonify({"success": False, "message": "Customer not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route("/update_inventory_details", methods=["POST"])
def update_inventory_details():
    try:
        data = request.form
        item_type = data.get("item_type")
        if not item_type:
            return jsonify({"success": False, "message": "Item Type is required for updating."})

        updates = []
        values = []

        for column in ["item_uom", "item_desc", "item_avl_qty", "item_ror", "item_value", "item_rate"]:
            value = data.get(column)
            if value:
                updates.append(f"`{column.replace('_', ' ').capitalize()}` = %s")
                values.append(value)

        if not updates:
            return jsonify({"success": False, "message": "At least one field should be provided to update."})

        query = f"""
            UPDATE `inventory`
            SET {', '.join(updates)}
            WHERE `Item Type` = %s
        """
        values.append(item_type)

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple(values))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Item updated successfully."})
        else:
            return jsonify({"success": False, "message": "No changes made or item not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route('/delete_item/<item_name>', methods=['DELETE'])
def delete_item(item_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("DELETE FROM inventory WHERE `Item Type` = %s", (item_name,))
        connection.commit()

        return jsonify({
            'success': True,
            'message': f'Item "{item_name}" deleted successfully.'
        })
    except Exception as e:
        connection.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
    finally:
        cursor.close()
        connection.close()

@app.route("/update_item_transaction_form", methods=["POST"])
def update_item_transaction_form():
    try:
        data = request.form
        item_type = data.get("item_type")
        if not item_type:
            return jsonify({"success": False, "message": "Item Type is required for updating."})

        updates = []
        values = []

        for column in ["item_uom", "item_desc", "item_avl_qty", "item_ror", "item_value", "item_rate"]:
            value = data.get(column)
            if value:
                updates.append(f"`{column.replace('_', ' ').capitalize()}` = %s")
                values.append(value)

        if not updates:
            return jsonify({"success": False, "message": "At least one field should be provided to update."})

        query = f"""
            UPDATE `invtrans`
            SET {', '.join(updates)}
            WHERE `Item Type` = %s
        """
        values.append(item_type)

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple(values))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Item updated successfully."})
        else:
            return jsonify({"success": False, "message": "No changes made or item not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route('/delete_itemtrns/<item_name>', methods=['DELETE'])
def delete_itemtrns(item_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("DELETE FROM invtrans WHERE `Item Type` = %s", (item_name,))
        connection.commit()

        return jsonify({
            'success': True,
            'message': f'Item "{item_name}" deleted successfully.'
        })
    except Exception as e:
        connection.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
    finally:
        cursor.close()
        connection.close()

###########

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
