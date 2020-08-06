# Vonage Internship Experience Innovation Challenge Winner - Safe Chat

**A burner phone application powered by Nexmo**

Codebase for Team 2, winner of 2018 VINE Innovation Challenge

[Kasey McFadden](https://www.linkedin.com/in/kaseymcfadden/), [Christine Mauro](https://www.linkedin.com/in/christine-mauro/), [Matthew Lu](https://www.linkedin.com/in/matt-lu/), [Regine Lewis](https://www.linkedin.com/in/regine-lewis-2a902310a/), [Ashna Momin](https://www.linkedin.com/in/ashna-momin-55a490141/)

------

## Demo Videos

[Academic Context Demo](https://drive.google.com/file/d/1sYojogOwENroZwGfyszMS4I8V22fZdmP/view?usp=sharing)

[Dating Context Demo](https://drive.google.com/file/d/1e95CS3PoCqch5SrClrj3eBz9L0nO0ZMi/view?usp=sharing)

------

## Requirements

1. Python 3
2. [Nexmo](https://nexmo.com/sign-up)
3. [IBM Watson](https://www.ibm.com/watson/)
4. [AWS Lambda, API Gateway, RDS DB Instance](https://aws.amazon.com/free/)

## Installation

#### 1. Clone this repository

`cd /path/to/repository/spot`

`git clone https://github.com/km-vonage/burner.git`

___

#### 2. Install Requirements

`pip install -t /path/to/burner -r requirements.txt`

___

#### 3. Create AWS Lambda function

[Create a new Lambda function](https://console.aws.amazon.com/lambda#/create/) > Author from scratch

_Basic information_

Name: **burner**

Runtime: **Python 3**

_Lambda function code_

Code entry type > **Upload a .ZIP file**

Upload > Compress and upload this cloned repository: **burner.zip**

_Lambda function handler and role_

Handler: **_interact.lambda_handler_**

Role > Choose an existing role: **IPA-Lambda**

_Advanced settings_

Memory: **128 MB**

Timeout: **6 sec**

___

#### 4. Create API in API Gateway

Edit swagger file: open **burner-swagger.json** > specify your AWS host (**"host", line 7**)

[Create an API](https://console.aws.amazon.com/apigateway#/apis/create)

Import from Swagger > Select Swagger File: **burner-swagger.json**

> Import 

Set up methods for **/auth**, **/auth/code**, **/interact**, and **/notifications**:

Integration type: **Lambda Function**

- [x] Use Lambda Proxy integration

Lambda Region: same region as Lambda Function

Lambda Function: **burner** 

> Save

Select Actions > Deploy API > **Deploy**

In the Stage Editor interface, take note of the **Invoke URL**.

___

#### 5. Create RDS Database

Use the commands in the `burner.ddl` file to create a new database with a table titled 'clients'.

Your 'clients' table will look something like this once users have registered for burner:

|      id       |  credentials  |
| ------------- |---------------|
| 12345678999   | google-creds  |
| 19876543210   | encoded-creds |

___

#### 6. Integrate Nexmo

Once you've registered for an account and have received a virtual number, [edit your number](https://dashboard.nexmo.com/your-numbers).

Webhook URL: **https:// INVOKE-URL /interact**

Ignore the voice options - these do not matter for our project.

___

#### 7. Integrate IBM Watson

Create a new [Watson Conversation Workspace](https://watson-conversation.ng.bluemix.net) by importing a workspace.

Choose **watson_workspace.json** and select Import Everything (Intents, Entities, and Dialog).

View the details of your imported workspace and take note of the **Workspace ID**.

Grab your Watson Conversation [Service Credentials](https://www.ibm.com/watson/developercloud/doc/common/getting-started-credentials.html) and keep track of these values.

___

## Credits

*A project by [Kasey McFadden](https://www.linkedin.com/in/kaseymcfadden), overseen by [Murali Ramsunder](https://www.linkedin.com/in/murali-ramsunder-5025856/), inspired by [Bismarck Paliz](https://www.linkedin.com/in/bismarckpaliz/)*

