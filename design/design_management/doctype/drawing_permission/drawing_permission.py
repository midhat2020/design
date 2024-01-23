# Copyright (c) 2024, Precihole and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class DrawingPermission(Document):
	def before_save(self):
		self.file_url = frappe.utils.get_url() + self.file_url
		if not doc.item_code:
			return
		frappe.db.get_value('File', {'attached_to_doctype': 'Item', 'attached_to_name': doc.item_code}, ['file_url'])
