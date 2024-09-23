# Deploying to GitHub Pages

## Step-by-Step Guide

    1. **Build the Site**: Ensure your build script (`build.js`) is run, and the `public` directory is up-to-date.

    ```sh
    node build.js
    ```

    2. Navigate to the public Directory: Change directory to public.

    ```sh
    cd public
    ```

    3. Initialise a New Git Repository in public: This will initialise a new Git repository specifically for the gh-pages branch.

    ```sh
    git init
    ```

    4. Add and Commit All Files: Add and commit all files in the public directory.

    ```sh
    git add .
    git commit -m "Deploy to gh-pages"
    ```

    5. Push to the gh-pages Branch: Push the contents of the public directory to the gh-pages branch on GitHub.

    ```sh
    git remote add origin https://github.com/username/repository-name.git
    git push --force origin main:gh-pages
    ```

## Automating the Deployment Process

To make the deployment process easier, you can create a script to automate these steps. Create a deploy.sh script in your root directory:

    ```sh
    #!/bin/bash

    # Run the build script
    node build.js

    # Navigate into the public directory
    cd public

    # Initialize a new git repository
    git init

    # Add and commit all the files
    git add .
    git commit -m "Deploy to gh-pages"

    # Force push to the gh-pages branch
    git push --force origin main:gh-pages

    # Navigate back to the root directory
    cd ..

    echo "Deployment to gh-pages branch complete."
    ```

Make sure to give execute permissions to the script:

    ```sh
    chmod +x deploy.sh
    ```

Now you can deploy your site to GitHub Pages by simply running:

    ```sh
    ./deploy.sh
    ```

## Summary

 • Build the Site: Ensure the public directory is up-to-date with the latest build.
 • Push Only the public Directory: The gh-pages branch should only contain the contents of the public directory.
 • Automate with a Script: Use a deployment script to streamline the process.