pipeline {
      agent any
      stages {
            stage('Checkout Code') {
                    steps {
                            checkout scm
                    }
            }
            stage('Extract Data') {
                    steps {
                        bat "C:\\Users\\Asus\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe extract.py"
                    
                    }
                            // Add build commands here
               }
        }
}