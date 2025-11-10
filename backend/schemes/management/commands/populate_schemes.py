import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from schemes.models import Scheme

class Command(BaseCommand):
    help = 'Populate database with sample government schemes'
    
    def handle(self, *args, **options):
        schemes_data = [
            {
                'name': 'PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)',
                'description': 'Direct income support to farmers',
                'scheme_type': 'CENTRAL',
                'category': 'AGRICULTURE',
                'ministry': 'Ministry of Agriculture & Farmers Welfare',
                'income_groups': ['EWS', 'LIG', 'MIG', 'OBC', 'SC', 'ST'],
                'applicable_states': [],  # All states
                'age_min': 18,
                'age_max': 100,
                'gender_applicable': ['MALE', 'FEMALE'],
                'benefits': '₹6000 per year in 3 installments of ₹2000 each',
                'eligibility_details': 'Small and marginal farmers with cultivable land',
                'required_documents': 'Aadhaar card, Bank account details, Land records',
                'application_process': 'Apply online at pmkisan.gov.in or visit CSC',
                'official_website': 'https://pmkisan.gov.in',
                'helpline_number': '155261',
                'is_active': True,
            },
            {
                'name': 'Pradhan Mantri Awas Yojana - Urban',
                'description': 'Housing scheme for urban poor',
                'scheme_type': 'CENTRAL',
                'category': 'HOUSING',
                'ministry': 'Ministry of Housing & Urban Affairs',
                'income_groups': ['EWS', 'LIG', 'MIG'],
                'applicable_states': [],
                'age_min': 21,
                'age_max': 70,
                'gender_applicable': ['MALE', 'FEMALE'],
                'benefits': 'Subsidy for home loans, houses at affordable rates',
                'eligibility_details': 'Urban residents without pucca house',
                'required_documents': 'Income certificate, Aadhaar, Bank details',
                'application_process': 'Apply through respective state implementing agency',
                'official_website': 'https://pmaymis.gov.in',
                'helpline_number': '011-23060484',
                'is_active': True,
            },
            {
                'name': 'Ayushman Bharat - Health and Wellness Centres',
                'description': 'Comprehensive primary healthcare',
                'scheme_type': 'CENTRAL',
                'category': 'HEALTH',
                'ministry': 'Ministry of Health & Family Welfare',
                'income_groups': ['EWS', 'LIG', 'OBC', 'SC', 'ST'],
                'applicable_states': [],
                'age_min': 0,
                'age_max': 100,
                'gender_applicable': ['MALE', 'FEMALE', 'OTHER'],
                'benefits': 'Free healthcare coverage up to ₹5 lakh per family',
                'eligibility_details': 'SECC 2011 beneficiaries and identified vulnerable families',
                'required_documents': 'Aadhaar card, SECC verification',
                'application_process': 'Automatic enrollment for eligible families',
                'official_website': 'https://pmjay.gov.in',
                'helpline_number': '14555',
                'is_active': True,
            },
            {
                'name': 'National Means-cum-Merit Scholarship',
                'description': 'Scholarship for economically weaker students',
                'scheme_type': 'CENTRAL',
                'category': 'EDUCATION',
                'ministry': 'Ministry of Education',
                'income_groups': ['EWS', 'LIG'],
                'applicable_states': [],
                'age_min': 13,
                'age_max': 18,
                'gender_applicable': ['MALE', 'FEMALE', 'OTHER'],
                'benefits': '₹12000 per year for class IX-XII students',
                'eligibility_details': 'Students from families with income below ₹1.5 lakh',
                'required_documents': 'Income certificate, Mark sheets, School certificate',
                'application_process': 'Apply through National Scholarship Portal',
                'official_website': 'https://scholarships.gov.in',
                'helpline_number': '0120-6619540',
                'is_active': True,
            },
            {
                'name': 'Karnataka Udyogini Scheme',
                'description': 'Entrepreneurship scheme for women in Karnataka',
                'scheme_type': 'STATE',
                'category': 'EMPLOYMENT',
                'ministry': 'Department of Women and Child Development, Karnataka',
                'income_groups': ['EWS', 'LIG', 'OBC', 'SC', 'ST'],
                'applicable_states': ['KA'],
                'age_min': 18,
                'age_max': 55,
                'gender_applicable': ['FEMALE'],
                'benefits': 'Loan up to ₹3 lakh at subsidized interest rates',
                'eligibility_details': 'Women entrepreneurs in Karnataka',
                'required_documents': 'Business plan, Income certificate, Karnataka domicile',
                'application_process': 'Apply through Karnataka State Women Development Corporation',
                'official_website': 'https://www.kswdc.kar.nic.in',
                'helpline_number': '080-22242035',
                'is_active': True,
            },
            {
                'name': 'Mahatma Gandhi NREGA',
                'description': 'Employment guarantee scheme for rural households',
                'scheme_type': 'CENTRAL',
                'category': 'EMPLOYMENT',
                'ministry': 'Ministry of Rural Development',
                'income_groups': ['EWS', 'LIG', 'OBC', 'SC', 'ST'],
                'applicable_states': [],
                'age_min': 18,
                'age_max': 100,
                'gender_applicable': ['MALE', 'FEMALE', 'OTHER'],
                'benefits': '100 days guaranteed wage employment per household per year',
                'eligibility_details': 'Rural households willing to do manual unskilled work',
                'required_documents': 'Job card, Aadhaar, Bank account details',
                'application_process': 'Apply at Gram Panchayat or online',
                'official_website': 'https://nrega.nic.in',
                'helpline_number': '1800-345-22-44',
                'is_active': True,
            },
        ]
        
        created_count = 0
        for scheme_data in schemes_data:
            scheme, created = Scheme.objects.get_or_create(
                name=scheme_data['name'],
                defaults=scheme_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created scheme: {scheme.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Scheme already exists: {scheme.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new schemes')
        )
