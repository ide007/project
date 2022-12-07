from django.db import models


class MainTable(models.Model):
    class Distinction(models.TextChoices):
        yes = 'ОТЛЧ',
        no = '---'

    # slug = models.SlugField(max_length=200, db_index=True)

    code_region_fbdp = models.IntegerField(
        verbose_name="Код региона-района ФБДП",
        blank=False,
        null=False,
        help_text="Код региона-района ФБДП",
    )

    code_region_last_change_ils = models.IntegerField(
        verbose_name="Код региона-района последнего изменения ИЛС",
        help_text="Код региона-района последнего изменения ИЛС",
        blank=False,
        null=False,
    )
    region_code_entry_info_about_death = models.IntegerField(
        verbose_name="Код региона внесения сведений о смерти",
        help_text="Код региона внесения сведений о смерти",
        blank=True,
        default=0,
    )
    region_code_ils_updating = models.IntegerField(
        verbose_name="Код региона актуализации ИЛС",
        help_text="Код региона актуализации ИЛС",
        default=0,
        blank=True,
    )
    snils = models.CharField(
        verbose_name="СНИЛС",
        help_text="СНИЛС",
        max_length=14,
        unique=True,
        blank=False,
        null=False,
    )
    new_snils = models.CharField(
        verbose_name="Новый СНИЛС (в случае УПРЗ)",
        help_text="Новый СНИЛС (в случае УПРЗ)",
        max_length=14,
        blank=True,
        default='',
    )
    identifier_fbdp = models.CharField(
        verbose_name="Идентификатор ФБДП",
        help_text="Идентификатор ФБДП",
        max_length=30,
        unique=True,
        blank=False,
        null=False,
    )
    surname_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Признак отличия фамилии",
        help_text="Признак отличия фамилии",
    )
    surname_spu = models.CharField(
        verbose_name="Фамилия СПУ",
        help_text="Фамилия СПУ",
        max_length=60,
        blank=True,
    )
    surname_fbdp = models.CharField(
        verbose_name="Фамилия ФБДП",
        help_text="Фамилия ФБДП",
        max_length=60,
        blank=True,
    )
    name_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Признак отличия имени",
        help_text="Признак отличия имени",
    )
    name_spu = models.CharField(
        verbose_name="Имя СПУ",
        help_text="Имя СПУ",
        max_length=20,
        blank=True,
    )
    name_fbdp = models.CharField(
        verbose_name="Имя ФБДП",
        help_text="Имя ФБДП",
        max_length=20,
        blank=True,
    )
    patronymic_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Признак отличия отчества",
        help_text="Признак отличия отчества",
    )
    patronymic_spu = models.CharField(
        verbose_name="Отчество СПУ",
        help_text="Отчество СПУ",
        max_length=20,
        blank=True,
        default='',
    )
    patronymic_fbdp = models.CharField(
        verbose_name="Отчество ФБДП",
        help_text="Отчество ФБДП",
        max_length=20,
        blank=True,
        default='',
    )
    gender_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Пол признак отличия",
        help_text="Пол признак отличия",
    )
    gender_spu = models.CharField(
        verbose_name="Пол СПУ",
        help_text="Пол СПУ",
        max_length=1,
        blank=False,
        null=False,
    )
    gender_fbdp = models.CharField(
        verbose_name="Пол ФБДП",
        help_text="Пол ФБДП",
        max_length=1,
        blank=False,
        null=False,
    )
    date_of_birth_distinction = models.CharField(
        max_length=4,
        choices=Distinction.choices,
        default=Distinction.no,
        verbose_name="Признак отличия даты рождения",
        help_text="Признак отличия даты рождения",
    )
    date_of_birth_spu = models.DateField(
        verbose_name="Дата рождения СПУ",
        help_text="Дата рождения СПУ",
        blank=False,
        null=False,
        # input_format="%d.%m.%Y",
    )
    date_of_birth_fbdp = models.DateField(
        verbose_name="Дата рождения ФБДП",
        help_text="Дата рождения ФБДП",
        blank=False,
        null=False,
        # input_format="%d.%m.%Y",
    )
    ils_status_distinction = models.CharField(
        max_length=4,
        verbose_name="Признак отличия статуса ИЛС",
        help_text="Признак отличия статуса ИЛС",
        choices=Distinction.choices,
        default=Distinction.no,
    )
    ils_status_spu = models.CharField(
        max_length=4,
        verbose_name="Статус ИЛС СПУ",
        help_text="Статус ИЛС СПУ",
        default='АКТЛ',
        blank=True,
    )
    ils_status_fbdp = models.CharField(
        max_length=4,
        verbose_name="Статус ИЛС ФБДП",
        help_text="Статус ИЛС ФБДП",
        default='АКТЛ',
        blank=True,
    )
    data_of_death_distinction = models.CharField(
        max_length=4,
        verbose_name="Признак отличия даты смерти",
        help_text="Признак отличия даты смерти",
        choices=Distinction.choices,
        default=Distinction.no,
    )
    data_of_death_spu = models.DateField(
        verbose_name="Дата смерти СПУ",
        help_text="Дата смерти СПУ",
        blank=True,
        null=True,
    )
    data_of_death_fbdp = models.DateField(
        verbose_name="Дата смерти ФБДП",
        help_text="Дата смерти ФБДП",
        blank=True,
        null=True,
    )
    document_id_code = models.IntegerField(
        verbose_name="Код документа удостоверяющего личность",
        help_text="Код документа удостоверяющего личность",
        blank=False,
    )
    document_spu = models.CharField(
        max_length=20,
        blank=False,
        verbose_name="Документ удостоверяющий личность СПУ",
        help_text="Документ удостоверяющий личность СПУ",
    )
    document_fbdp = models.CharField(
        max_length=20,
        blank=False,
        verbose_name="Документ удостоверяющий личность ФБДП",
        help_text="Документ удостоверяющий личность ФБДП",
    )
    document_seria_distinction = models.CharField(
        max_length=4,
        verbose_name="Признак отличия серии ДУЛ",
        help_text="Признак отличия серии ДУЛ",
        choices=Distinction.choices,
        default=Distinction.no,
    )
    document_seria_spu = models.CharField(
        max_length=10,
        verbose_name="Серия ДУЛ СПУ",
        help_text="Серии ДУЛ СПУ",
        blank=False,
    )
    document_seria_fbdp = models.CharField(
        max_length=10,
        verbose_name="Серия ДУЛ ФБДП",
        help_text="Серии ДУЛ ФБДП",
        blank=False,
    )
    document_number_distinction = models.CharField(
        max_length=4,
        verbose_name="Признак отличия номера ДУЛ",
        help_text="Признак отличия номера ДУЛ",
        choices=Distinction.choices,
        default=Distinction.no,
    )
    document_number_spu = models.CharField(
        max_length=10,
        verbose_name="Номер ДУЛ СПУ",
        help_text="Номер ДУЛ СПУ",
        blank=False,
    )
    document_number_fbdp = models.CharField(
        max_length=10,
        verbose_name="Номер ДУЛ ФБДП",
        help_text="Номер ДУЛ ФБДП",
        blank=False,
    )
    date_of_issue_document_distinction = models.CharField(
        max_length=4,
        verbose_name="Признак отличия даты выдачи ДУЛ",
        help_text="Признак отличия даты выдачи ДУЛ",
        choices=Distinction.choices,
        default=Distinction.no,
    )
    date_of_issue_document_spu = models.DateField(
        verbose_name="Дата выдачи ДУЛ СПУ",
        help_text="Дата выдачи ДУЛ СПУ",
        blank=False,
        # input_format="%Y-%m-%d",
    )
    date_of_issue_document_fbdp = models.DateField(
        verbose_name="Дата выдачи ДУЛ ФБДП",
        help_text="Дата выдачи ДУЛ ФБДП",
        blank=False,
        # input_format="%Y-%m-%d",
    )
    who_issued_spu = models.CharField(
        max_length=200,
        verbose_name="Кем выдан ДУЛ СПУ",
        help_text="Кем выдан ДУЛ СПУ",
        blank=True,
        default="",
    )
    who_issued_fbdp = models.CharField(
        max_length=200,
        verbose_name="Кем выдан ДУЛ ФБДП",
        help_text="Кем выдан ДУЛ ФБДП",
        blank=True,
        default="",
    )
    place_of_birth_spu = models.CharField(
        max_length=100,
        blank=True,
        default="",
        verbose_name="Место рождения СПУ",
        help_text="Место рождения СПУ",
    )
    place_of_birth_fbdp = models.CharField(
        max_length=100,
        blank=True,
        default="",
        verbose_name="Место рождения ФБДП",
        help_text="Место рождения ФБДП",
    )
    date_of_change_status_ils_spu = models.DateField(
        verbose_name="Дата изменения статуса ИЛС СПУ",
        help_text="Дата изменения статуса ИЛС СПУ",
        blank=True,
        null=True,
    )
    date_of_change_personal_data_spu = models.DateField(
        verbose_name="Дата изменения анкетных данных в СПУ",
        help_text="Дата изменения анкетных данных в СПУ",
        blank=True,
        null=True,
    )
    date_include_info_about_death_ils = models.DateField(
        verbose_name="Дата включения сведений о смерти в ИЛС",
        help_text="Дата включения сведений о смерти в ИЛС",
        blank=True,
        null=True,
    )
    source_of_death_info = models.CharField(
        max_length=50,
        verbose_name="Источник получения сведений о смерти",
        help_text="Источник получения сведений о смерти",
        blank=True,
    )
    source_info_update_in_ils = models.CharField(
        max_length=50,
        verbose_name="Источник получения сведений об актуализации ИЛС",
        help_text="Источник получения сведений об актуализации ИЛС",
        blank=True,
    )
    act_number = models.CharField(
        max_length=10,
        verbose_name="Номер актовой записи",
        help_text="Номер актовой записи",
        blank=True,
    )
    date_act_number = models.DateField(
        verbose_name="Дата актовой записи",
        help_text="Дата актовой записи",
        blank=True,
        null=True,
    )
    date_transfer_change_in_exd = models.DateField(
        verbose_name="Дата передачи изменений в ЕХД",
        help_text="Дата передачи изменений в ЕХД",
        blank=True,
        null=True,
    )
    date_transfer_info_from_nvp_to_fbdp = models.DateField(
        verbose_name="Дата передачи сведений из НВП в ФБДП",
        help_text="Дата передачи сведений из НВП в ФБДП",
        blank=True,
        null=True,
    )
    date_issue_reference_of_death = models.DateField(
        verbose_name="Дата выдачи справки о смерти",
        help_text="Дата выдачи справки о смерти",
        blank=True,
        null=True,
    )
    number_of_issue_of_death_reference = models.CharField(
        max_length=20,
        verbose_name="Номер справки о смерти",
        help_text="Номер справки о смерти",
        blank=True,
    )
    number_of_certificate_of_death = models.CharField(
        max_length=20,
        verbose_name="Номер свидетельства о смерти",
        help_text="Номер свидетельства о смерти",
        blank=True,
    )
    date_start_inshure_pensii = models.DateField(
        verbose_name="Дата назначения страховой пенсии",
        help_text="Дата назначения страховой пенсии",
        blank=True,
        null=True,
    )
    region_nvp = models.IntegerField(
        verbose_name="Район НВП",
        blank=True,
        default="",
        null=True,
        help_text="Район НВП",
    )
    type_inshure_pensii = models.CharField(
        verbose_name="Вид страховой пенсии",
        help_text="Вид страховой пенсии",
        blank=True,
        max_length=30,
    )
    zl_in_work = models.CharField(
        verbose_name="ЗЛ, находящихся в работе",
        help_text="ЗЛ, находящихся в работе",
        blank=True,
        max_length=30,
    )
    refactor_cell = models.IntegerField(
        verbose_name="Расхождения устранены",
        help_text="Расхождения устранены",
        blank=True,
        default=0,
    )
    refactor_in_spu = models.IntegerField(
        verbose_name="Уточнены данные в ПС СПУ",
        help_text="Уточнены данные в ПС СПУ",
        blank=True,
        default=0,
    )
    refactor_in_fbdp = models.IntegerField(
        verbose_name="Уточнены данные в ПС ФБДП",
        help_text="Уточнены данные в ПС ФБДП",
        blank=True,
        default=0,
    )
    not_needed_refactoring = models.CharField(
        verbose_name="Не требуется проведения работ",
        help_text="Не требуется проведения работ",
        blank=True,
        max_length=150,
    )
    reason_witch_not_needed = models.CharField(
        verbose_name="Причина, по которой проведение работ не требуется",
        help_text="Причина, по которой проведение работ не требуется",
        blank=True,
        max_length=150,
    )
    responsible_department = models.CharField(
        verbose_name="Ответственный отдел",
        help_text="Ответственный отдел",
        blank=True,
        max_length=100,
    )
    correction_mark = models.IntegerField(
        verbose_name="Отметка о корректировке",
        help_text="Отметка о корректировке",
        blank=True,
        default=0,
    )

    def __str__(self):
        return f'{self.pk} | {self.snils}: {self.surname_spu} {self.name_spu} {self.patronymic_spu}'

    class Meta:
        verbose_name = "Запись таблицы"
        verbose_name_plural = "Общая таблица"
