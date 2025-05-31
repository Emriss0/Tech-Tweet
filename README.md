# Tech-Tweet 🚀

![Tech-Tweet](https://img.shields.io/badge/Tech--Tweet-Django-blue.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg) ![MySQL](https://img.shields.io/badge/MySQL-5.7%2B-orange.svg) ![Bootstrap](https://img.shields.io/badge/Bootstrap-4.5%2B-purple.svg)

Welcome to **Tech-Tweet**, a Django-based microblogging app designed for tech enthusiasts. With Tech-Tweet, users can share their thoughts on technology, engage with others, and explore the latest trends in the tech world. This README will guide you through the features, installation, usage, and contribution guidelines for the project.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Releases](#releases)

## Features 🌟

- **User Authentication**: Secure sign-up and login processes to protect user data.
- **Post Short Tech Tweets**: Share your thoughts in a tweet-like format.
- **Commenting System**: Engage in discussions by commenting on posts.
- **Like/Dislike Posts**: Express your opinion on tweets with likes and dislikes.
- **Interaction Stats**: View statistics on your posts and interactions.
- **Responsive Design**: Built with Bootstrap for a seamless experience on any device.
- **Simple Feed**: A clean feed to share ideas and connect with the community.

## Installation 🛠️

To set up Tech-Tweet on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Emriss0/Tech-Tweet.git
   cd Tech-Tweet
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Make sure you have MySQL installed.
   - Create a database named `tech_tweet`.
   - Update the `settings.py` file with your database credentials.

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the App**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage 💻

Once you have the app running, you can start using it by following these steps:

1. **Sign Up**: Create an account by providing your email and password.
2. **Log In**: Use your credentials to log in.
3. **Create a Tweet**: Use the input box to share your tech thoughts.
4. **Engage with Others**: Comment on tweets, and like or dislike posts.
5. **View Stats**: Check the interaction stats on your profile.

## Technologies Used ⚙️

- **Django**: The main framework for building the application.
- **Python**: The programming language used for backend development.
- **MySQL**: The database management system for storing user data and tweets.
- **Bootstrap**: For responsive and attractive UI design.
- **HTML5/CSS3**: For structuring and styling the web pages.
- **JavaScript**: For enhancing interactivity.

## Contributing 🤝

We welcome contributions to Tech-Tweet! If you want to help improve the project, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**: Go to the original repository and click on "New Pull Request".

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Releases 📦

To check for the latest releases, visit [Tech-Tweet Releases](https://github.com/Emriss0/Tech-Tweet/releases). Here, you can download the latest version of the app and execute it on your machine.

## Conclusion 🎉

Thank you for checking out Tech-Tweet! We hope you find it useful for sharing your tech thoughts and engaging with the community. If you have any questions or feedback, feel free to reach out or contribute to the project. Happy tweeting!