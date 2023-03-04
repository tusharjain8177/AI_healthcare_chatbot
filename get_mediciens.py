mediciens = {'gastroenteritis': ['ondansetron',
  'doxycycline',
  'ceftriaxone',
  'ampicillin',
  'rotavirus vaccine'],
 'migraine': ['sumatriptan',
  'rizatriptan',
  'onabotulinumtoxinA',
  'rimegepant',
  'ubrogepant'],
 'malaria': ['artemether / lumefantrine',
  'hydroxychloroquine',
  'chloroquine',
  'doxycycline',
  'mefloquine'],
 'pneumonia': ['levofloxacin',
  'clarithromycin',
  'ceftriaxone',
  'azithromycin',
  'doxycycline'],
 'hyperthyroidism': ['methimazole',
  'propylthiouracil',
  'potassium iodide',
  'iodine / potassium iodide',
  'sodium iodide-i-131'],
 'acne': ['doxycycline',
  'spironolactone',
  'minocycline',
  'clindamycin',
  'tretinoin'],
 'urinary-tract-infection': ['nitrofurantoin',
  'ciprofloxacin',
  'sulfamethoxazole / trimethoprim',
  'amoxicillin',
  'doxycycline'],
 'psoriasis': ['clobetasol',
  'methotrexate',
  'triamcinolone',
  'guselkumab',
  'ixekizumab'],
 'impetigo': ['mupirocin',
  'cefadroxil',
  'cefuroxime',
  'retapamulin',
  'ozenoxacin']}



def get_mediciens(disease):
    if disease in mediciens:
        return mediciens[disease]
    else:
        return "No medicine found for this disease"

name = get_mediciens("gastroenteritis")
print(name)