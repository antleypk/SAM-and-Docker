SAM and Docker

This is a simple docker and SAM (AWS Serverless Application Model) application.  This automatically deploys an application to aws. The sam and docker combo make for a quick and easy automated deployment pattern.  The application as a whole, grabs data from a publically viewable s3 bucket. It downloads the data from an .xlsx converts it to a .csv.  Then two s3 buckets are created. After the buckets are created the SAM template is used to build a cloudformation stack. Three lambda functions are connected with three api endpoints. The first lambda function returns a large json without aggregation. The second one performs a simple count of how many rows are present. The final lambda function performs a simple 'group by' style action.  There are many ways that this logic can be re-arranged to aggregate or slice the data in any way desired. I built this as a POC project and would welcome any feedback; and answer any questions any future developers may have.  

::developers take note:: there is no primary key on for the data being presented. 

::developers take note:: this docker file will spin up aws resources if used correctly. They will bill you.

:: aws cli docker / sam :: I chose to use utilize enviromental variables for this project to feed into the creation of the docker. While there may be other ways to do this; the enviromental variable method used here worked well for me. 
