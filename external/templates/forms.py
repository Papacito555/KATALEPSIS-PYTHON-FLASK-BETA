from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import StringField, TextField, RadioField, SelectField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired

COLLABORATORS_CHOICES = [('min_collaborators', '1 a 15'),
                         ('medium_collaborators', '16 a 50'),
                         ('many_collaborators', 'Más de 51')]

SECTOR_CHOICES = [('sector1', 'Mostrar Sectores'),
                  ('sector2', 'Metalurgia'),
                  ('sector3', 'Informática'),
                  ('sector4', 'Industrial'),
                  ('sector5', 'Alimentos'),
                  ('sector6', 'Mineria'),
                  ]

SEXO = [('hombre', 'Masculino'), ('mujer', 'Femenino')]

CIVIL_STATUS = [('casado', 'Casad@'), ('soltero', 'Solter@'),
                ('divorciado', 'Divorciad@'), ('libre', 'Unión Libre'),
                ('viduo', 'Viud@')]

JOB = [('1', 'Administrativo'), ('2', 'Gerente/Director'),
       ('3', 'Operativo'), ('4', 'Profesional o técnico'),
       ('5', 'Supervisor/Coordinador')]

DEGREE = [('1', 'Sin Estudios'), ('2', 'Primaria Trunca'),
          ('3', 'Primaria terminada'), ('4', 'Secundaria Trunca'),
          ('5', 'Secundaria completa'), ('6', 'Bachillerato Trunco'),
          ('7', 'Bachillerato Completo'), ('8', 'Técnico Superior Incompleto'),
          ('9', 'Técnico Superior Completo'), ('10', 'Licenciatura Trunca'),
          ('11', 'Licenciatura completa'), ('12', 'Maestria Trunca'),
          ('13', 'Maestria Completa'), ('14', 'Doctorado Trunco'),
          ('15', 'Doctorado Completo')]

CONTRACT = [('Obra', 'Por Obra o Proyecto'), ('tiempodet', 'Por Tiempo Determinado (Temporal)'),
            ('tiempoinder', 'Por Tiempo Indeterminado'), ('honores', 'Honorarios')
            ]

PERSONAL = [('sindicalizado', 'Sindicalizado'), ('Fijo', 'Fijo'), ('Otros', 'Otros')
            ]

JOURNEY = [('Nocturno', 'Nocturno (Entre 20:00 y 06:00)'), ('Diurno', 'Diurno(Entre 06:00 y 20:00)'),
           ('Diurno', 'Diurno(Entre 06:00 y 20:00)'), ('Mixto', 'Mixto (Combinación entre nocturno y diurno)'),
           ('jornada', 'Otros (Especifique en el siguiente campo)')
           ]

PERSONAL_EXPERIENCE = [('1', 'Menos de 6 meses'), ('2', 'Entre 6 meses y un año'),
                       ('3', 'Entre 1 a 4 años'), ('4', 'Entre 4 y 9 años'),
                       ('5', 'Entre 9 a 14 años'), ('6', 'Entre 14 a 19 años'),
                       ('7', 'Entre 19 a 24 años'), ('8', '25 años o más'),
                       ]
LINE_CHOICES = [('pending', 'Pendiente'), ('build', 'Construcción'),
                ('finish', 'Terminado'), ('review', 'Revisión'),
                ('deployment', 'Implementado')
                ]


class CompanyForm(FlaskForm):
    # Step 1
    nameCompany = StringField('Nombre de la empresa',
                              validators=[DataRequired()],
                              render_kw={"placeholder": "Empresa"})
    collaborators = RadioField('Numero de colaboradores',
                               choices=COLLABORATORS_CHOICES,
                               default='min_collaborators',
                               validators=[DataRequired()])
    bussinessSector = SelectField('Sector Empresarial',
                                  choices=SECTOR_CHOICES,
                                  validators=[DataRequired()])
    directContact = StringField('Puesto de contacto directo',
                                validators=[DataRequired()],
                                render_kw={"placeholder": "Ing. Sergio Fuenlabrada"})
    email = EmailField('Correo Electronico',
                       validators=[DataRequired()],
                       render_kw={"placeholder": "name@example.com"})
    hasCertificates = RadioField('¿Cuenta con certificaciones?',
                                 choices=[('certificate_yes', 'Si'), ('certificate_no', 'No')],
                                 validators=[DataRequired()])
    knownNom035 = RadioField('¿Conoce la NOM 0-35?',
                             choices=[('known_nom_35_yes', 'Si'), ('known_nom_35_no', 'No')],
                             validators=[DataRequired()])
    

    # Step 2
    nameCollaborator = StringField('Nombre',
                                   validators=[DataRequired()],
                                   render_kw={"placeholder": "Nombre del Colaborador"})

    sex = SelectField('Sexo', choices=SEXO, validators=[DataRequired()])

    civilStatus = SelectField('Estado Civil',
                              choices=CIVIL_STATUS,
                              validators=[DataRequired()])

    job = SelectField('Puesto', choices=JOB, validators=[DataRequired()])

    personalEmail = StringField('Correo electrónico Personal',
                                validators=[DataRequired()],
                                render_kw={"placeholder": "name@example.com"})

    phone = StringField('Telefono',
                        validators=[DataRequired()],
                        render_kw={"placeholder": "5546789012"})

    academicDegree = SelectField('Nivel de Estudios', choices=DEGREE, validators=[DataRequired()])

    # Step 3
    profession = StringField('Ocupación/Profesión/Puesto (De acuerdo al Organigrama):',
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Director Ejecutivo"})
    department = StringField('Departamento/Sección/Área (De acuerdo al Organigrama):',
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Gerencia"})
    workstation = SelectField('Puesto', choices=JOB, validators=[DataRequired()])

    contractType = SelectField('Contrato', choices=CONTRACT,
                               validators=[DataRequired()])

    personalType = SelectField('Tipo de Personal:', choices=PERSONAL,
                               validators=[DataRequired()])

    especificarPersonal = StringField('Especifica:', render_kw={"placeholder": "Otro"})

    laboralJourney = SelectField('Tipo de Jornada Laboral:',
                                 choices=JOURNEY,
                                 validators=[DataRequired()])

    specificJourney = StringField('Especifica:', render_kw={"placeholder": "Otro"})

    shiftRotation = SelectField('¿Realiza rotación de turnos?',
                                choices=[('Nocturno', 'Si'), ('Diurno', 'No')],
                                validators=[DataRequired()])

    experience = StringField('Experiencia (Años):',
                             validators=[DataRequired()],
                             render_kw={"placeholder": "5 años"})

    currentPosition = SelectField('Tiempo en puesto actual:',
                                  choices=PERSONAL_EXPERIENCE,
                                  validators=[DataRequired()])

    laboralExperience = SelectField('Experiencia Laboral:',
                                    choices=PERSONAL_EXPERIENCE,
                                    validators=[DataRequired()])

    # Step 4
    knowledgeNom035 = RadioField('¿Conoce la NOM 0-35?',
                                 choices=LINE_CHOICES,
                                 validators=[DataRequired()])
    requerimentsStp = RadioField('¿Conoce cuales son los requisitos que nos pide cumplir la STPS?',
                                 choices=LINE_CHOICES,
                                 validators=[DataRequired()])
    ftpsField = RadioField(
        '¿Establece,implanta, y mantiene una politica de prevención de Factores de Riesgo Psico Sociales (FRPS)?',
        choices=LINE_CHOICES,
        validators=[DataRequired()])
    eofField = RadioField(
        '¿Cuenta con medidas de prevención de los FRPS, la violencia laboral y promoción de un Entorno Organizacional Favorable (EOF)?',
        choices=LINE_CHOICES,
        validators=[DataRequired()])
    implementField = RadioField('¿Tiene integrado un comité de implementación?',
                                choices=LINE_CHOICES,
                                validators=[DataRequired()])
    recomendationsField = RadioField(
        '¿Cuenta con mecanismos seguros y confidenciales para la recepción de quejas de sus colaboradores?',
        choices=LINE_CHOICES,
        validators=[DataRequired()])
    atsField = RadioField(
        '¿Mantiene identificados a los trabajadores sujetos a Acontencimientos Traumaticos Severos (ATS) durante o con motivo del trabajo?',
        choices=LINE_CHOICES,
        validators=[DataRequired()])
    securityField = RadioField(
        '¿Canaliza a los trabajadores identificados con (ATS) a la seguridad o privada, o con el médico de la empresa?',
        choices=LINE_CHOICES,
        validators=[DataRequired()])
    frpsField = RadioField('¿Tiene asertivamente identificado los FRPS y EOF?',
                           choices=LINE_CHOICES,
                           validators=[DataRequired()])
    reportField = RadioField('¿Cuenta con informes de resultados de la identificación y analisis de los FRPS y EOF?',
                             choices=LINE_CHOICES,
                             validators=[DataRequired()])
    perdiodField = RadioField('¿Informa periodicamente de los resultados obtenidos a sus colaboradores?',
                              choices=LINE_CHOICES,
                              validators=[DataRequired()])
    analysisField = RadioField('¿Realiza la identificación y analisis al menos cada año?',
                               choices=LINE_CHOICES,
                               validators=[DataRequired()])
    psycologyField = RadioField(
        '¿Practica examenes médicos y evaluaciones psicologicas al trabajador que ha sido detectado como expuesto?',
        choices=LINE_CHOICES,
        validators=[DataRequired()])
    surveyField = RadioField('¿Cuenta con implementación de encuestas en las guias de referencia de la NOM 35?',
                             choices=LINE_CHOICES,
                             validators=[DataRequired()])
    controlField = RadioField('¿Cuenta con un programa de control y atención a primero,segundo y tercer nivel?',
                              choices=LINE_CHOICES,
                              validators=[DataRequired()])

    submit = SubmitField('Enviar Formulario')
