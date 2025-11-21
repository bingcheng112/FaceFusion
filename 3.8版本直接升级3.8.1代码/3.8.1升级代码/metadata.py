from typing import Optional

METADATA =\
{
	'name': 'FaceFusionFree',
	'description': 'Industry leading face manipulation platform',
	'version': 'VIP3.8.1',
	'license': 'OpenRAIL-AS',
	'author': 'Henry Ruhs',
	'url': 'https://www.youtube.com/@wangzhifengAI'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
