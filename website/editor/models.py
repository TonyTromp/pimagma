from django.db import models

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Driver(models.Model):
    Classifier = models.CharField(unique=False, max_length=5)
    Title = models.CharField(max_length=60, blank=True)
    Description = models.TextField(max_length=256)
    def __str__(self):
        return self.Classifier + ' | ' + self.Title

class BusinessDriver(Driver):
    Title = ''

class ComplianceDriver(Driver):
    Title = ''

class ThreatModel(models.Model):
    class Meta:
        app_label = 'My App Label'
        abstract = True
                
class Threat(models.Model):
    Classifier = models.CharField(unique=False, max_length=4)
    Title = models.CharField(max_length=60, blank=True)
    Description = models.TextField(max_length=256)

#Tactics
class L1StrategicalThreat(Threat, models.Model):
    RiskDriver = models.ManyToManyField("Driver", blank=True)
    def __str__(self):
        return self.Classifier + ' | ' + self.Title
 
    def __unicode__(self):
        return self.Classifier +' | '+ self.Title

    def as_dict(self):
        return { "ID": self.id,
          "Classifier": self.Classifier,
          "Title": self.Title,
          "Description": self.Description 
        } 
    

#Techniques
class L2TacticalThreat(Threat, models.Model):
    Parent = models.ForeignKey(L1StrategicalThreat, on_delete=models.CASCADE)

    def get_class(self):
        return self.Parent.Classifier +'-'+ self.Classifier

    def __str__(self):
        return self.Parent.Classifier +'-'+ self.Classifier + ' | ' + self.Title

    def as_dict(self):
        return {
          "ID": self.id,
          "Classifier": self.Parent.Classifier +'-'+ self.Classifier,
          "Title": self.Title,
          "Description": self.Description, 
          "Parent": { 
             "ID": self.Parent.id
          }
        } 

class SecurityLayer(models.Model):
    Title = models.CharField(max_length=60, blank=True)
    Description = models.TextField(max_length=256)
    def __str__(self):
        return self.Title
    
class SecurityControl(models.Model):
    Title = models.CharField(max_length=60, blank=True)
    Description = models.TextField(max_length=512)
    Layer = models.ManyToManyField("SecurityLayer", blank=True)    
    def __str__(self):
        return self.Title

class SecurityPerimeter(models.Model):
    Title = models.CharField(max_length=60, blank=True)
    Description = models.TextField(max_length=512)
    def __str__(self):
        return self.Title

class L3OperationalThreat(Threat):
    Parent = models.ForeignKey(L2TacticalThreat, on_delete=models.CASCADE)    

    Effectiveness  = IntegerRangeField(min_value=1, max_value=100);
    Implementation = IntegerRangeField(min_value=1, max_value=100);
    Coverage = IntegerRangeField(min_value=1, max_value=100);

    SecurityControl = models.ManyToManyField("SecurityControl", blank=True, verbose_name='Security Control')    
    SecurityPerimeter = models.ManyToManyField("SecurityPerimeter", blank=True, verbose_name='Perimeter')    
   
    def __str__(self):
        return self.Parent.Parent.Classifier +'-'+ self.Parent.Classifier +'-'+ self.Classifier + ' | ' + self.Title

    def as_dict(self):
        return {
          "ID": self.id,
          "Classifier": self.Parent.Classifier +'-'+ self.Classifier,
          "Title": self.Title,
          "Description": self.Description, 
          "Parent": { 
             "ID": self.Parent.id
          }
        } 


#    ThreatCoverage  = models.ManyToManyField(L2TacticalThreat, null=True, blank=True)




