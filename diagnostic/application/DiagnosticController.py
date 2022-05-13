from flask import Flask, Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from external.templates import forms
from diagnostic.core.models.diagnostic import DiagnosticDB
from diagnostic.core.models.diagnostic import db

controller = Blueprint('home_page', __name__,
                       template_folder='../../external/templates',
                       static_folder='../../external/static',
                       static_url_path='/')


@controller.route('/')
def home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@controller.route('/diagnostic', methods=['GET', 'POST'])
def diagnostic():
    company_form = forms.CompanyForm(request.form)

    if company_form.validate_on_submit():
        try:

            diagnosticDB = DiagnosticDB(company_form.data["nameCompany"],
                    company_form.data["collaborators"],
                    company_form.data["bussinessSector"],
                    company_form.data["directContact"],
                    company_form.data["email"],
                    company_form.data["hasCertificates"],
                    company_form.data["knownNom035"],
                    company_form.data["nameCollaborator"],
                    company_form.data["sex"],
                    company_form.data["civilStatus"],
                    company_form.data["job"],
                    company_form.data["personalEmail"],
                    company_form.data["phone"],
                    company_form.data["academicDegree"],
                    company_form.data["profession"],
                    company_form.data["department"],
                    company_form.data["workstation"],
                    company_form.data["contractType"],
                    company_form.data["personalType"],
                    company_form.data["especificarPersonal"],
                    company_form.data["laboralJourney"],
                    company_form.data["specificJourney"],
                    company_form.data["shiftRotation"],
                    company_form.data["experience"],
                    company_form.data["currentPosition"],
                    company_form.data["laboralExperience"],
                    company_form.data["knowledgeNom035"],
                    company_form.data["requerimentsStp"],
                    company_form.data["ftpsField"],
                    company_form.data["eofField"],
                    company_form.data["implementField"],
                    company_form.data["recomendationsField"],
                    company_form.data["atsField"],
                    company_form.data["securityField"],
                    company_form.data["frpsField"],
                    company_form.data["reportField"],
                    company_form.data["perdiodField"],
                    company_form.data["analysisField"],
                    company_form.data["psycologyField"],
                    company_form.data["surveyField"],
                    company_form.data["controlField"])
            print(diagnosticDB)
            db.session.add(diagnosticDB)
            db.session.commit()

            return render_template('index.html')        
        except TemplateNotFound:
            abort(404)

    return render_template('diagnostic.html', form=company_form)
