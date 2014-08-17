# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2013 OpenERP s.a. (<http://openerp.com>).
#    Copyright (C) 2014 copado MEDIA UG (<http://www.copado.de>).
#    Author Mathias Neef <mn[at]copado.de>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Deutschland - Accounting IKR',
    'version': '1.0',
    'author': 'copado MEDIA',
	'website': 'http://www.copado.de',
    'category': 'Localization/Account Charts',
    'description': """
Dieses Modul beinhaltet den deutschen Kontenrahmen IKR (Industriekontenrahmen) angelehnt an den Schulkontenrahmen der IHK.
==========================================================================================================================
	* Letzte Überarbeitung IKR: 08/2014


English:
German accounting chart and localization (Industry Chart Temlate (IKR)) relating to the school-chart-template of the IHK (Industry and Trade Chamber).
	* Last change IKR: 08/2014

    """,
    'depends': [
		'base',
		'account',
		'base_iban',
		'base_vat',
		'account_chart'
	],
    'demo': [],
    'data': [
        'account_tax_ikr.xml',
        'account_chart_schema_ikr.xml',
        'account_chart_ikr.xml', 					
        'account_chart_template_ikr.xml',			
        'account_tax_fiscal_position_ikr.xml',		
        'chart_ikr_wizard.xml',
    ],
    'installable': True,
    'images': ['images/config_chart_l10n_de.jpeg','images/l10n_de_chart.jpeg'],
}

