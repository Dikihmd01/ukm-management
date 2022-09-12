from odoo import api, fields, models


class IncomingLetter(models.Model):
    _name = 'ccstmiktsm.incomingletter'
    _description = 'Surat Masuk'

    name = fields.Char(string='Judul Surat')
    incoming_code = fields.Char(string='Kode Surat Masuk',
                                readonly=True,
                                copy=False,
                                required=True,
                                default='New')
    letter_from = fields.Selection(string='Dari',
                                    selection=[('LFM', 'LFM'),
                                                ('Homeband', 'Homebans'),
                                                ('Mapalas', 'Mapalas'),
                                                ('FDK', 'FDK'),
                                                ('BEM', 'BEM'),
                                                ('Padus', 'Padus'),
                                                ('MB', 'Marching Band')])
    
    sender_name = fields.Char(string='Nama Pengirim')
    date_incoming = fields.Date(string='Tanggal',
                                default=fields.Datetime.now())
    received_by = fields.Char(string='Nama Penerima',
                                required=True)
    


    @api.model
    def create(self, vals):
        if vals.get('incoming_code', 'New') == 'New':
            vals['incoming_code'] = self.env['ir.sequence'].next_by_code(
                'ccstmiktsm.incomingletter' or 'New'
            )

        result = super(IncomingLetter, self).create(vals)
        return result
