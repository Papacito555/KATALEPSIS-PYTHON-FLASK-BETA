from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yXR~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sofnityPass@localhost/katalepsis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class DiagnosticDB(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    nameCompany = db.Column(db.String(250))
    collaborators = db.Column(db.String(250))
    bussinessSector = db.Column(db.String(250))
    directContact = db.Column(db.String(250))
    email = db.Column(db.String(250))
    hasCertificates = db.Column(db.String(250))
    knownNom035 = db.Column(db.String(250))
    nameCollaborator = db.Column(db.String(250))
    sex = db.Column(db.String(250))
    civilStatus = db.Column(db.String(250))
    job = db.Column(db.String(250))
    personalEmail = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    academicDegree = db.Column(db.String(250))
    profession = db.Column(db.String(250))
    department = db.Column(db.String(250))
    workstation = db.Column(db.String(250))
    contractType = db.Column(db.String(250))
    personalType = db.Column(db.String(250))
    especificarPersonal = db.Column(db.String(250))
    laboralJourney = db.Column(db.String(250))
    specificJourney = db.Column(db.String(250))
    shiftRotation = db.Column(db.String(250))
    experience = db.Column(db.String(250))
    currentPosition = db.Column(db.String(250))
    laboralExperience = db.Column(db.String(250))
    knowledgeNom035 = db.Column(db.String(250))
    requerimentsStp = db.Column(db.String(250))
    ftpsField = db.Column(db.String(250))
    eofField = db.Column(db.String(250))
    implementField = db.Column(db.String(250))
    recomendationsField = db.Column(db.String(250))
    atsField = db.Column(db.String(250))
    securityField = db.Column(db.String(250))
    frpsField = db.Column(db.String(250))
    reportField = db.Column(db.String(250))
    perdiodField = db.Column(db.String(250))
    analysisField = db.Column(db.String(250))
    psycologyField = db.Column(db.String(250))
    surveyField = db.Column(db.String(250))
    controlField = db.Column(db.String(250))
    

    def __init__(self, nameCompany, collaborators,bussinessSector,directContact,
        email,hasCertificates,knownNom035,nameCollaborator,sex,
        civilStatus,job,personalEmail,phone,degree,profession,department,
        workstation,contractType,personalType,especificarPersonal,laboralJourney,
        specificJourney,shiftRotation,experience,currentPosition,laboralExperience,
        knowledgeNom035,requerimentsStp,ftpsField,eofField,implementField,
        recomendationsField,atsField,securityField,frpsField,reportField,perdiodField,
        analysisField,psycologyField,surveyField,controlField):
        self.nameCompany = nameCompany
        self.collaborators = collaborators
        self.bussinessSector = bussinessSector
        self.directContact = directContact
        self.email = email
        self.hasCertificates = hasCertificates
        self.knownNom035 = knownNom035
        self.nameCollaborator = nameCollaborator
        self.sex = sex
        self.civilStatus = civilStatus
        self.job = job
        self.personalEmail = personalEmail
        self.phone = phone
        self.degree = degree
        self.profession = profession
        self.department = department
        self.workstation = workstation
        self.contractType = contractType
        self.personalType = personalType
        self.especificarPersonal = especificarPersonal
        self.laboralJourney = laboralJourney
        self.specificJourney = specificJourney
        self.shiftRotation = shiftRotation
        self.experience = experience
        self.currentPosition = currentPosition
        self.laboralExperience = laboralExperience
        self.knowledgeNom035 = knowledgeNom035
        self.requerimentsStp = requerimentsStp
        self.ftpsField = ftpsField
        self.eofField = eofField
        self.implementField = implementField
        self.recomendationsField = recomendationsField
        self.atsField = atsField
        self.securityField = securityField
        self.frpsField = frpsField
        self.reportField = reportField
        self.perdiodField = perdiodField
        self.analysisField = analysisField
        self.psycologyField = psycologyField
        self.surveyField = surveyField
        self.controlField = controlField

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},'.format(self.nameCompany,
            self.collaborators,
            self.bussinessSector,
            self.directContact,
            self.email,
            self.hasCertificates,
            self.knownNom035,
            self.nameCollaborator,
            self.sex,
            self.civilStatus,
            self.job,
            self.personalEmail,
            self.phone,
            self.degree,
            self.profession,
            self.department,
            self.workstation,
            self.contractType,
            self.personalType,
            self.especificarPersonal,
            self.laboralJourney,
            self.specificJourney,
            self.shiftRotation,
            self.experience,
            self.currentPosition,
            self.laboralExperience,
            self.knowledgeNom035,
            self.requerimentsStp,
            self.ftpsField,
            self.eofField,
            self.implementField,
            self.recomendationsField,
            self.atsField,
            self.securityField,
            self.frpsField,
            self.reportField,
            self.perdiodField,
            self.analysisField,
            self.psycologyField,
            self.surveyField,
            self.controlField)