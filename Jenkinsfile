
pipeline {
    agent any

    environment {
        DEV_REPO = 'conan-releases'
        TAG_FILE = "${WORKSPACE}/tag.json"
		ARTEFACT_NAME="compressor"
        BUILD_DIR = "./build"
    }

    stages {

        stage ('Install dependencies'){
            steps {
                sh 'pwd'
                sh 'rm -rf ${BUILD_DIR}'
            }
            post {
                success {
                    sh 'echo Now installing dependencies...'
                    sh 'conan install . --output-folder=${BUILD_DIR} --build=missing'
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
						dir("${BUILD_DIR}"){
							sh 'cmake --build .'
						}
					}
				}
		}
				
		stage('Test'){
				steps {
					dir("${BUILD_DIR}"){
						sh './${ARTEFACT_NAME}'
					}
				}
		}

        stage('Create tag'){
            steps {
                script {
    
                    // Git data (Git plugin)
                    echo "${GIT_COMMIT}"
                    echo "${GIT_URL}"
                    echo "${GIT_BRANCH}"
                    echo "${WORKSPACE}"
                    
                    // construct the meta data (Pipeline Utility Steps plugin)
                    def tagdata = readJSON text: '{}' 
                    tagdata.buildUser = "${USER}" as String
                    tagdata.buildNumber = "${BUILD_NUMBER}" as String
                    tagdata.buildId = "${BUILD_ID}" as String
                    tagdata.buildJob = "${JOB_NAME}" as String
                    tagdata.buildTag = "${BUILD_TAG}" as String
                    tagdata.appVersion = "${BUILD_VERSION}" as String
                    tagdata.buildUrl = "${BUILD_URL}" as String
                    tagData.promote = "no" as String

                    writeJSON(file: "${TAG_FILE}", json: tagdata, pretty: 4)

                    createTag nexusInstanceId: 'nxrm3', tagAttributesPath: "${TAG_FILE}", tagName: "${BUILD_TAG}"

                    // write the tag name to the build page (Rich Text Publisher plugin)
                    rtp abortedAsStable: false, failedAsStable: false, parserName: 'Confluence', stableText: "Nexus Repository Tag: ${BUILD_TAG}", unstableAsStable: true 
                }
            }
			post {
				success {
              	    sh 'echo tag_file: && cat ${TAG_FILE}'
				}
			}
        }
       
        


    }
}                   


