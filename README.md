# Apollo Solutions - Backend

<font size="3">**Setup and Running the Project**</font>

<font size="2">1 - Clone the repository to your local machine. On the VS Code console or any other IDE of your preference, use this command: git clone https://github.com/JorgeHCamara/backend</font> \
<font size="2">2 - Navigate to the project directory: cd backend</font> \
<font size="2">3 - Set up a virtual environment (bash console | make sure that the bash console is also on the python-app directory): python -m venv venv</font> \
<font size="2">4 - Activate the virtual environment: .\venv\Scripts\activate (Windows) or source venv/bin/activate (Mac and Linux)</font> \
<font size="2">5 - Install the required Python packages (bash console): pip install -r requirements.txt</font> \
<font size="2">6 - To run the application on your local machine (bash console): python app.py</font>

# Answers

<font size="3">1. What would be your first improvements if you had more implementation time?</font> \
<font size="2">Thinking about the scalability of the project, I would implement pagination, so the system would be prepared for a larger number of products registered in terms of both user experience and performance. I would also implement an authentication system, so only authorized people could add and delete products on the platform.</font>

<font size="3">2. Thinking about your solution, how would maintenance be in case of adding new product categories? What would need to be changed?</font> \
<font size="2">Currently, you would only need to add a new Menu Item option to the Select Input of the FilterSection.tsx file, because the 'category' property in the Product model in the API expects any string. However, for organization, security and best coding practices, it would be better to prepare the API to only receive certain types of categories, for example by transforming the 'category' property of the Product model into an Enum.</font>

<font size="3">3. What changes would need to be made to support updates in the product category's discount percentage so that whenever the discount percentage was changed, the new price would be reflected in all products of the same category?</font> \
<font size="2">Now, it's not currently possible to change an already registered product's promotional price because this is being handled statically in the DiscountService.ts. Therefore, if the discount percentage is changed there, it would only affect newly registered products. A lot of changes would be necessary in both the frontend and backend to make this proccess dynamic and ensure that all products, old and new, reflect the updated discount percentages.</font>
