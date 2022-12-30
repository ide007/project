from django import forms
from django.db import models
from django.urls import reverse

from mainapp.models import MainTable


class Distinction(models.TextChoices):
    yes = 'ОТЛЧ',
    no = '---'


class MainTableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__()

    class Meta:
        model = MainTable
        fields = '__all__'
        # fields = ['code_region_fbdp', 'code_region_last_change_ils', 'region_code_entry_info_about_death',
        #           'region_code_ils_updating', 'snils', 'new_snils', 'identifier_fbdp', 'surname_distinction',
        #           'surname_spu', 'surname_fbdp', 'name_distinction', 'name_spu', 'name_fbdp', 'patronymic_distinction',
        #           'patronymic_spu', 'patronymic_fbdp', 'gender_distinction', 'gender_spu', 'gender_fbdp',
        #           'date_of_birth_distinction', 'date_of_birth_spu', 'date_of_birth_fbdp', 'ils_status_distinction',
        #           'ils_status_spu', 'ils_status_fbdp', 'data_of_death_distinction', 'data_of_death_spu',
        #           'data_of_death_fbdp', 'document_id_code', 'document_spu', 'document_fbdp',
        #           'document_seria_distinction', 'document_seria_spu', 'document_seria_fbdp',
        #           'document_number_distinction', 'document_number_spu', 'document_number_fbdp',
        #           'date_of_issue_document_distinction', 'date_of_issue_document_spu', 'date_of_issue_document_fbdp',
        #           'who_issued_spu', 'who_issued_fbdp', 'place_of_birth_spu', 'place_of_birth_fbdp',
        #           'date_of_change_status_ils_spu', 'date_of_change_personal_data_spu',
        #           'date_include_info_about_death_ils', 'source_of_death_info', 'source_info_update_in_ils',
        #           'act_number', 'date_act_number', 'date_transfer_change_in_exd', 'date_transfer_info_from_nvp_to_fbdp',
        #           'date_issue_reference_of_death', 'number_of_issue_of_death_reference',
        #           'number_of_certificate_of_death', 'date_start_inshure_pensii', 'region_nvp', 'type_inshure_pensii',
        #           'zl_in_work', 'refactor_cell', 'refactor_in_spu', 'refactor_in_fbdp', 'not_needed_refactoring',
        #           'reason_witch_not_needed', 'responsible_department', 'correction_mark']
        # widgets = {'code_region_fbdp': forms.IntegerField(max_value=99999),
        #            'code_region_last_change_ils': forms.IntegerField(max_value=99999),
        #            'region_code_entry_info_about_death': forms.IntegerField(max_value=99999),
        #            'region_code_ils_updating': forms.IntegerField(max_value=99999),
        #            'snils': forms.CharField(max_length=14, min_length=14),
        #            'new_snils': forms.CharField(max_length=14, min_length=14),
        #            'identifier_fbdp': forms.CharField(max_length=30, min_length=30),
        #            'surname_distinction': forms.CharField(choices=Distinction.choices, max_length=4),
        #            'surname_spu': forms.CharField(max_length=60), 'surname_fbdp': forms.CharField(max_length=60),
        #            'name_distinction': forms.CharField(choices=Distinction.choices, max_length=4),
        #            'name_spu': forms.CharField(max_length=20), 'name_fbdp': forms.CharField(max_length=20),
        #            'patronymic_distinction': forms.CharField(choices=Distinction.choices, max_length=4),
        #            'patronymic_spu': forms.CharField(max_length=20), 'patronymic_fbdp': forms.CharField(max_length=20),
        #            'gender_distinction': forms.CharField(choices=Distinction.choices, max_length=4),
        #            'gender_spu': forms.CharField(max_length=7), 'gender_fbdp': forms.CharField(max_length=7),
        #            'date_of_birth_distinction': forms.CharField(choices=Distinction.choices, max_length=4),
        #            'date_of_birth_spu': forms.DateField(), 'date_of_birth_fbdp': forms.DateField(),
        #            'ils_status_distinction': forms.CharField(choices=Distinction.choices, max_length=4),
        #            'ils_status_spu': forms.CharField(max_length=4, default='АКТЛ'),
        #            'ils_status_fbdp': forms.CharField(max_length=4, default='АКТЛ'),
        #            # 'data_of_death_distinction':, 'data_of_death_spu',
        #            # 'data_of_death_fbdp', 'document_id_code', 'document_spu', 'document_fbdp',
        #            # 'document_seria_distinction', 'document_seria_spu', 'document_seria_fbdp',
        #            # 'document_number_distinction', 'document_number_spu', 'document_number_fbdp',
        #            # 'date_of_issue_document_distinction', 'date_of_issue_document_spu', 'date_of_issue_document_fbdp',
        #            # 'who_issued_spu', 'who_issued_fbdp', 'place_of_birth_spu', 'place_of_birth_fbdp',
        #            # 'date_of_change_status_ils_spu', 'date_of_change_personal_data_spu',
        #            # 'date_include_info_about_death_ils', 'source_of_death_info', 'source_info_update_in_ils',
        #            # 'act_number', 'date_act_number', 'date_transfer_change_in_exd', 'date_transfer_info_from_nvp_to_fbdp',
        #            # 'date_issue_reference_of_death', 'number_of_issue_of_death_reference',
        #            # 'number_of_certificate_of_death', 'date_start_inshure_pensii', 'region_nvp', 'type_inshure_pensii',
        #            # 'zl_in_work', 'refactor_cell', 'refactor_in_spu', 'refactor_in_fbdp', 'not_needed_refactoring',
        #            # 'reason_witch_not_needed', 'responsible_department', 'correction_mark'
        # }

        def __str__(self):
            return self.snils

        def get_absolute_url(self):
            return reverse('post', kwargs={'post_id': self.id})