from email.policy import default
from odoo import api, fields, models


class Member(models.Model):
    _inherit = 'res.partner'
    _description = 'Anggota'

    CHOICES = [
        ('SE', 'Software Engineer'),
        ('PD', 'Product Design'),
        ('BA', 'Business Analyst'),
    ]

    npm = fields.Char(string='NPM')
    major = fields.Char(string='Jurusan')
    division = fields.Selection(string='Divisi',
                                selection=CHOICES,
                                default='SE')
    state = fields.Selection(string='Status',
                            selection=[('aktif', 'Aktif'),
                                        ('pasif', 'Pasif'),
                                        ('keluar', 'keluar')],
                            default='aktif',
                            required=True)
    batch = fields.Char(string='Angkatan')

