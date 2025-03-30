# DIY Instruction API

This is a REST API for managing DIY (Do It Yourself) projects, categories, and tags. It allows users to create, read, update, and delete DIY projects, as well as manage categories and tags.

## Features

*   **DIY Project Management:**
    *   Create new DIY projects.
    *   Retrieve a list of all DIY projects (with pagination).
    *   Retrieve details of a specific DIY project.
    *   Update existing DIY projects.
    *   Delete DIY projects.
*   **Category Management:**
    *   Create new categories.
    *   Retrieve a list of all categories.
*   **Tag Management:**
    *   Create new tags.
    *   Retrieve a list of all tags.
*   **RESTful API:** Uses a RESTful architecture for easy integration with various clients.
*   **Serialization:** Uses Django REST Framework serializers to convert data to and from JSON.
*   **Pagination:** Implements pagination for list views to handle large datasets efficiently.
*   **Filtering:** Supports filtering of DIY projects by category and tags.
*   **Authentication:** (Currently Removed) Originally implemented authentication using JWT (JSON Web Tokens) or Django's default authentication.  This has been removed for simplicity, but can be re-implemented.
*   **Permissions:** (Currently Removed) Originally implemented permissions to allow read-only access for everyone and require authentication for modifications. This has been removed for simplicity, but can be re-implemented.
*   **Testing:** Includes a comprehensive set of unit tests for models, serializers, and API endpoints.

## Technologies Used

*   Python
*   Django
*   Django REST Framework
*   django-filter
*   (Originally) djangorestframework-jwt

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd diy-instruction-api
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    *   On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

*   `GET /api/projects/`: List all DIY projects (supports pagination and filtering).
*   `POST /api/projects/`: Create a new DIY project.
*   `GET /api/projects/<id>/`: Retrieve details of a specific DIY project.
*   `PUT /api/projects/<id>/`: Update an existing DIY project.
*   `DELETE /api/projects/<id>/`: Delete a DIY project.
*   `GET /api/categories/`: List all categories.
*   `POST /api/categories/`: Create a new category.
*   `GET /api/tags/`: List all tags.
*   `POST /api/tags/`: Create a new tag.

## Testing

To run the unit tests, use the following command:

```bash
python manage.py test projects
