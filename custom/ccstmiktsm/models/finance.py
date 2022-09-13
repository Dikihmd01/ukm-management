from odoo import api, fields, models


class Balance(models.Model):
    _name = 'ccstmiktsm.balance'
    _description = 'Saldo'

    name = fields.Char(string='Periode')
    saldo = fields.Integer(
        string='Saldo',
        compute='_compute_saldo'
    )
    income_ids = fields.One2many(
        comodel_name='ccstmiktsm.income',
        inverse_name='balance_id',
        string='Pemasukan'
    )
    
    @api.depends('income_ids')
    def _compute_saldo(self):
        for line in self:
            result = sum(self.env['ccstmiktsm.income'].search(
                [('balance_id', '=', line.id)]).mapped('new_income'))
            line.saldo = result


class Income(models.Model):
    _name = 'ccstmiktsm.income'
    _description = 'Pemasukan'

    name = fields.Char(string='Keterangan')
    date_in = fields.Date(string='Tanggal')
    income_code = fields.Char(
        string='Kode Pemasukan',
        readonly=True,
        copy=False,
        required=True,
        default='New'
    )

    @api.model
    def get_balance(self):
        return self.env['ccstmiktsm.balance'].search(
            [(
                'income_ids', '=', self.id
            )]
        )

    balance_id = fields.Many2one(
        comodel_name='ccstmiktsm.balance',
        string='Saldo',
        default=get_balance
    )
    new_income = fields.Integer(string='Jumlah')
   
    @api.model
    def create(self, vals):
        if vals.get('income_code', 'New') == 'New':
            vals['income_code'] = self.env['ir.sequence'].next_by_code(
                'ccstmiktsm.income' or 'New'
            )

        result = super(Income, self).create(vals)
        return result

