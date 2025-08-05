
pipeline {
    agent any

    environment {
        DEV_REPO = 'conan-releases'
        TAG_FILE = "${WORKSPACE}/tag.json"
		ARTEFACT_NAME="compressor"
        BUILD_DIR = "./build"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pwd'
                sh 'rm -rf ${BUILD_DIR}'
            }
            post {
                success {
                    sh 'echo 'Now installing dependencies...'
                    sh 'conan install . --output-folder=${BUILD_DIR} --build-missing'
                }
            }
        }
        

		stage('Build') {
				steps {
					dir("${BUILD_DIR}"){
						sh 'cmake .. -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release'
					}
				}
				post {
					success {
						dir("${BUILD_DIR}") {
							sh 'cmake --build .'
						}
					}
				}
		}
				
		stage('Test'){
				steps {
					dir("${BUILD_DIR}") {
						sh './$(ARTEFACT_NAME)'
					}
				}
		}
    }

}

