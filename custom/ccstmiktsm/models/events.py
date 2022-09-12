from odoo import api, fields, models


class Events(models.Model):
    _name = 'ccstmiktsm.event'
    _description = 'Acara'

    CHOICES = [
        ('SE', 'Software Engineer'),
        ('PD', 'Product Design'),
        ('BA', 'Business Analyst'),
        ('ccpasif', 'CC Pasif'),
        ('external', 'External'),
    ]

    name = fields.Char(string='Nama kegiatan')
    event_code = fields.Char(string='Kode acara',
                            readonly=True,
                            copy=False,
                            required=True,
                            default='New')
    event_type_id = fields.Many2one(comodel_name='ccstmiktsm.eventtype',
                                    string='Jenis kegiatan',
                                    required=True)
    speaker = fields.Char(string='Pemateri',
                            required=True)
    division_of_speaker = fields.Selection(string='Asal pemateri',
                                            selection=CHOICES,
                                            required=True)
    event_date = fields.Date(string='Tanggal',
                            default=fields.Datetime.now())
    place = fields.Char(string='Tempat')
    
    @api.model
    def create(self, vals):
        if vals.get('event_code', 'New') == 'New':
            vals['event_code'] = self.env['ir.sequence'].next_by_code(
                'ccstmiktsm.event' or 'New'
            )

        result = super(Events, self).create(vals)
        return result
