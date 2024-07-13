# Task Manager API

#### Description

Task Manager API is a task management system that uses Django as the backend and ArangoDB as the database. The system provides user and job management functions, user authorization, and endpoint protection using JWT.

#### Main features

1. Register, log in, log out (including refresh token and log out from other devices).
2. Decentralize user rights with three types: Admin, Manager, User:

- Admin: Manage all jobs and users.
- Manager: Manage the work of yourself and the Users under you.
- User: Manage personal work.

3. Add, edit, delete and view task lists according to user permissions.
4. Job information includes: Title, Description, Start date, End date, Status.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Docker
- Python 3.8+
- Node.js (for Yarn)

### Installation

1. Clone repository:

```bash
git clone <repository_url>
cd task_manager
```

2. Create .env file from .env.example and update the necessary information:

```bash
cp .env.example .env
cp .env.example .env.prod
```

3. Install dependencies:

```bash
yarn install
```

### Running the Application

#### Development

```bash
yarn dev
```

This command will start the Django server with auto-reload and connect to the development database specified in .env.

#### Production

```bash
yarn prod
```

This command will start the Django server optimized for production environment.

### Stopping the Application

To stop the running Docker containers:

```bash
yarn down
```

### Code Formatting and Linting

```bash
yarn lint
```

To format your Python code using Black:

```bash
yarn format
```

### Configuration

Make sure to configure your environment variables in `.env` file. Here is an example configuration:

```dotenv
# Environment variables for Django project

# Django settings
SECRET_KEY=your_secret_key
DEBUG=False

# ArangoDB settings
ARANGO_DB_URL=http://arangodb:8529
ARANGO_DB_NAME=task_manager_dev
ARANGO_DB_USERNAME=root
ARANGO_DB_PASSWORD=root
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
