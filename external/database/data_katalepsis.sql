CREATE DATABASE katalepsis;

CREATE TABLE diagnosticDB (
    user_id serial PRIMARY KEY, nameCompany VARCHAR ( 250 ) , 
    collaborators VARCHAR ( 250 ) , bussinessSector VARCHAR ( 250 ) , 
    directContact VARCHAR ( 250 ) , email VARCHAR ( 250 ) , 
    hasCertificates VARCHAR ( 250 ) , knownNom035 VARCHAR ( 250 ) , 
    nameCollaborator VARCHAR ( 250 ) , sex VARCHAR ( 250 ) , 
    civilStatus VARCHAR ( 250 ) , job VARCHAR ( 250 ) , 
    personalEmail VARCHAR ( 250 ) , phone VARCHAR ( 250 ) , 
    academicDegree VARCHAR ( 250 ) , profession VARCHAR ( 250 ) , 
    department VARCHAR ( 250 ) , workstation VARCHAR ( 250 ) , 
    contractType VARCHAR ( 250 ) , personalType VARCHAR ( 250 ) , 
    especificarPersonal VARCHAR ( 250 ) , laboralJourney VARCHAR ( 250 ) , 
    specificJourney VARCHAR ( 250 ) , shiftRotation VARCHAR ( 250 ) , 
    experience VARCHAR ( 250 ) , currentPosition VARCHAR ( 250 ) , 
    laboralExperience VARCHAR ( 250 ) , knowledgeNom035 VARCHAR ( 250 ) , 
    requerimentsStp VARCHAR ( 250 ) , ftpsField VARCHAR ( 250 ) , 
    eofField VARCHAR ( 250 ) , implementField VARCHAR ( 250 ) , 
    recomendationsField VARCHAR ( 250 ) , atsField VARCHAR ( 250 ) , 
    securityField VARCHAR ( 250 ) , frpsField VARCHAR ( 250 ) , 
    reportField VARCHAR ( 250 ) , perdiodField VARCHAR ( 250 ) , 
    analysisField VARCHAR ( 250 ) , psycologyField VARCHAR ( 250 ) , 
    surveyField VARCHAR ( 250 ) , controlField VARCHAR ( 250 )		
);

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `age` int(11) NOT NULL DEFAULT '0',
  `email` varchar(255) NOT NULL,
  `photo` varchar(255) DEFAULT 'default.png',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;