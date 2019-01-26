Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
  ?State Name           MLB Team(s)     ...      Unnamed: 12  Unnamed: 13
0     Arizona  Arizona Diamondbacks     ...              NaN          NaN
1  California    Los Angeles Angels     ...              NaN          NaN
2  California   Los Angeles Dodgers     ...              NaN          NaN
3  California           Oakland A's     ...              NaN          NaN
4  California      San Diego Padres     ...              NaN          NaN

[5 rows x 14 columns]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
       ?State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 10, in <module>
    avg = df_mlb.groupby('state').mean()
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 6665, in groupby
    observed=observed, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 2152, in groupby
    return klass(obj, by, **kwds)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 599, in __init__
    mutated=self.mutated)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 3291, in _get_grouper
    raise KeyError(gpr)
KeyError: 'state'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
       ?State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 10, in <module>
    avg = df_mlb.groupby('state')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 6665, in groupby
    observed=observed, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 2152, in groupby
    return klass(obj, by, **kwds)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 599, in __init__
    mutated=self.mutated)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 3291, in _get_grouper
    raise KeyError(gpr)
KeyError: 'state'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
       ?State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 10, in <module>
    avg = df_mlb.groupby('state')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 6665, in groupby
    observed=observed, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 2152, in groupby
    return klass(obj, by, **kwds)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 599, in __init__
    mutated=self.mutated)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 3291, in _get_grouper
    raise KeyError(gpr)
KeyError: 'state'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
       ?State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 9, in <module>
    avg = df_mlb.groupby('State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 6665, in groupby
    observed=observed, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 2152, in groupby
    return klass(obj, by, **kwds)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 599, in __init__
    mutated=self.mutated)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 3291, in _get_grouper
    raise KeyError(gpr)
KeyError: 'State'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
       ?State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 10, in <module>
    avg = df_mlb.State.unique()
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'State'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
       ?State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 10, in <module>
    avg = df_mlb.State.unique()
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'State'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
[('Arizona',      State                  Team    ...     start_point  end_point
0  Arizona  Arizona Diamondbacks    ...            1998       2018

[1 rows x 5 columns]), ('California',         State                  Team    ...     start_point  end_point
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004
5  California      San Diego Padres    ...            2005       2018
6  California  San Francisco Giants    ...            1998       1999
7  California  San Francisco Giants    ...            2000       2018

[7 rows x 5 columns]), ('Colorado',       State              Team stadium_zipcode  start_point  end_point
8  Colorado  Colorado Rockies           80204         1998       1994
9  Colorado  Colorado Rockies           80205         1998       2018), ('Florida',       State            Team stadium_zipcode  start_point  end_point
10  Florida   Miami Marlins           33056         1998       2011
11  Florida   Miami Marlins           33125         2012       2018
12  Florida  Tampa Bay Rays           33705         1998       2018), ('Georgia',       State            Team stadium_zipcode  start_point  end_point
13  Georgia  Atlanta Braves           30312         1998       1996
14  Georgia  Atlanta Braves           30315         1998       2016
15  Georgia  Atlanta Braves           30339         2017       2018), ('Illinois',        State               Team    ...     start_point  end_point
16  Illinois       Chicago Cubs    ...            1998       2018
17  Illinois  Chicago White Sox    ...            1998       1990
18  Illinois  Chicago White Sox    ...            1991       2018

[3 rows x 5 columns]), ('Maryland',        State               Team    ...     start_point  end_point
19  Maryland  Baltimore Orioles    ...            1998       2018

[1 rows x 5 columns]), ('Massachusetts',             State            Team    ...     start_point  end_point
20  Massachusetts  Boston Red Sox    ...            1998       2018

[1 rows x 5 columns]), ('Michigan',        State            Team stadium_zipcode  start_point  end_point
21  Michigan  Detroit Tigers           48216         1998       1999
22  Michigan  Detroit Tigers           48201         2000       2018), ('Minnesota',         State             Team    ...     start_point  end_point
23  Minnesota  Minnesota Twins    ...            1998       2009
24  Minnesota  Minnesota Twins    ...            2010       2018

[2 rows x 5 columns]), ('Missouri',        State                 Team    ...     start_point  end_point
25  Missouri   Kansas City Royals    ...            1998       2018
26  Missouri  St. Louis Cardinals    ...            1998       2005
27  Missouri  St. Louis Cardinals    ...            2006       2018

[3 rows x 5 columns]), ('Montreal, Quebec, Canada',                        State   Team    ...     start_point  end_point
46  Montreal, Quebec, Canada  Expos    ...            1998       2004

[1 rows x 5 columns]), ('New York',        State              Team    ...     start_point  end_point
28  New York     New York Mets    ...            1998       2008
29  New York     New York Mets    ...            2009       2018
30  New York  New York Yankees    ...            1998       2008
31  New York  New York Yankees    ...            2009       2018

[4 rows x 5 columns]), ('Ohio',    State               Team stadium_zipcode  start_point  end_point
32  Ohio  Cleveland Indians           44115         1998       2018
33  Ohio    Cincinnati Reds           45202         1998       2002
34  Ohio    Cincinnati Reds           45202         2003       2018), ('Pennsylvania',            State                   Team    ...     start_point  end_point
35  Pennsylvania  Philadelphia Phillies    ...            1998       2003
36  Pennsylvania  Philadelphia Phillies    ...            2004       2018
37  Pennsylvania     Pittsburgh Pirates    ...            1998       2000
38  Pennsylvania     Pittsburgh Pirates    ...            2001       2018

[4 rows x 5 columns]), ('Texas',     State            Team stadium_zipcode  start_point  end_point
39  Texas  Houston Astros           77054         1998       1999
40  Texas  Houston Astros           77002         2000       2018
41  Texas   Texas Rangers           76011         1998       2018), ('Washington',          State              Team    ...     start_point  end_point
42  Washington  Seattle Mariners    ...            1998       1999
43  Washington  Seattle Mariners    ...            2000       2018

[2 rows x 5 columns]), ('Washington DC',             State                  Team    ...     start_point  end_point
47  Washington DC  Washington Nationals    ...            2005       2007
48  Washington DC  Washington Nationals    ...            2008       2018

[2 rows x 5 columns]), ('Wisconsin',         State               Team    ...     start_point  end_point
44  Wisconsin  Milwaukee Brewers    ...            1998       2000
45  Wisconsin  Milwaukee Brewers    ...            2001       2018

[2 rows x 5 columns])]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 10, in <module>
    state = df_mlb.groupby('State').unique()
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 765, in __getattr__
    (type(self).__name__, attr))
AttributeError: 'DataFrameGroupBy' object has no attribute 'unique'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
[('Arizona',      State                  Team    ...     start_point  end_point
0  Arizona  Arizona Diamondbacks    ...            1998       2018

[1 rows x 5 columns]), ('California',         State                  Team    ...     start_point  end_point
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004
5  California      San Diego Padres    ...            2005       2018
6  California  San Francisco Giants    ...            1998       1999
7  California  San Francisco Giants    ...            2000       2018

[7 rows x 5 columns]), ('Colorado',       State              Team stadium_zipcode  start_point  end_point
8  Colorado  Colorado Rockies           80204         1998       1994
9  Colorado  Colorado Rockies           80205         1998       2018), ('Florida',       State            Team stadium_zipcode  start_point  end_point
10  Florida   Miami Marlins           33056         1998       2011
11  Florida   Miami Marlins           33125         2012       2018
12  Florida  Tampa Bay Rays           33705         1998       2018), ('Georgia',       State            Team stadium_zipcode  start_point  end_point
13  Georgia  Atlanta Braves           30312         1998       1996
14  Georgia  Atlanta Braves           30315         1998       2016
15  Georgia  Atlanta Braves           30339         2017       2018), ('Illinois',        State               Team    ...     start_point  end_point
16  Illinois       Chicago Cubs    ...            1998       2018
17  Illinois  Chicago White Sox    ...            1998       1990
18  Illinois  Chicago White Sox    ...            1991       2018

[3 rows x 5 columns]), ('Maryland',        State               Team    ...     start_point  end_point
19  Maryland  Baltimore Orioles    ...            1998       2018

[1 rows x 5 columns]), ('Massachusetts',             State            Team    ...     start_point  end_point
20  Massachusetts  Boston Red Sox    ...            1998       2018

[1 rows x 5 columns]), ('Michigan',        State            Team stadium_zipcode  start_point  end_point
21  Michigan  Detroit Tigers           48216         1998       1999
22  Michigan  Detroit Tigers           48201         2000       2018), ('Minnesota',         State             Team    ...     start_point  end_point
23  Minnesota  Minnesota Twins    ...            1998       2009
24  Minnesota  Minnesota Twins    ...            2010       2018

[2 rows x 5 columns]), ('Missouri',        State                 Team    ...     start_point  end_point
25  Missouri   Kansas City Royals    ...            1998       2018
26  Missouri  St. Louis Cardinals    ...            1998       2005
27  Missouri  St. Louis Cardinals    ...            2006       2018

[3 rows x 5 columns]), ('Montreal, Quebec, Canada',                        State   Team    ...     start_point  end_point
46  Montreal, Quebec, Canada  Expos    ...            1998       2004

[1 rows x 5 columns]), ('New York',        State              Team    ...     start_point  end_point
28  New York     New York Mets    ...            1998       2008
29  New York     New York Mets    ...            2009       2018
30  New York  New York Yankees    ...            1998       2008
31  New York  New York Yankees    ...            2009       2018

[4 rows x 5 columns]), ('Ohio',    State               Team stadium_zipcode  start_point  end_point
32  Ohio  Cleveland Indians           44115         1998       2018
33  Ohio    Cincinnati Reds           45202         1998       2002
34  Ohio    Cincinnati Reds           45202         2003       2018), ('Pennsylvania',            State                   Team    ...     start_point  end_point
35  Pennsylvania  Philadelphia Phillies    ...            1998       2003
36  Pennsylvania  Philadelphia Phillies    ...            2004       2018
37  Pennsylvania     Pittsburgh Pirates    ...            1998       2000
38  Pennsylvania     Pittsburgh Pirates    ...            2001       2018

[4 rows x 5 columns]), ('Texas',     State            Team stadium_zipcode  start_point  end_point
39  Texas  Houston Astros           77054         1998       1999
40  Texas  Houston Astros           77002         2000       2018
41  Texas   Texas Rangers           76011         1998       2018), ('Washington',          State              Team    ...     start_point  end_point
42  Washington  Seattle Mariners    ...            1998       1999
43  Washington  Seattle Mariners    ...            2000       2018

[2 rows x 5 columns]), ('Washington DC',             State                  Team    ...     start_point  end_point
47  Washington DC  Washington Nationals    ...            2005       2007
48  Washington DC  Washington Nationals    ...            2008       2018

[2 rows x 5 columns]), ('Wisconsin',         State               Team    ...     start_point  end_point
44  Wisconsin  Milwaukee Brewers    ...            1998       2000
45  Wisconsin  Milwaukee Brewers    ...            2001       2018

[2 rows x 5 columns])]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
[('Arizona',      State                  Team    ...     start_point  end_point
0  Arizona  Arizona Diamondbacks    ...            1998       2018

[1 rows x 5 columns]), ('California',         State                  Team    ...     start_point  end_point
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004
5  California      San Diego Padres    ...            2005       2018
6  California  San Francisco Giants    ...            1998       1999
7  California  San Francisco Giants    ...            2000       2018

[7 rows x 5 columns]), ('Colorado',       State              Team stadium_zipcode  start_point  end_point
8  Colorado  Colorado Rockies           80204         1998       1994
9  Colorado  Colorado Rockies           80205         1998       2018), ('Florida',       State            Team stadium_zipcode  start_point  end_point
10  Florida   Miami Marlins           33056         1998       2011
11  Florida   Miami Marlins           33125         2012       2018
12  Florida  Tampa Bay Rays           33705         1998       2018), ('Georgia',       State            Team stadium_zipcode  start_point  end_point
13  Georgia  Atlanta Braves           30312         1998       1996
14  Georgia  Atlanta Braves           30315         1998       2016
15  Georgia  Atlanta Braves           30339         2017       2018), ('Illinois',        State               Team    ...     start_point  end_point
16  Illinois       Chicago Cubs    ...            1998       2018
17  Illinois  Chicago White Sox    ...            1998       1990
18  Illinois  Chicago White Sox    ...            1991       2018

[3 rows x 5 columns]), ('Maryland',        State               Team    ...     start_point  end_point
19  Maryland  Baltimore Orioles    ...            1998       2018

[1 rows x 5 columns]), ('Massachusetts',             State            Team    ...     start_point  end_point
20  Massachusetts  Boston Red Sox    ...            1998       2018

[1 rows x 5 columns]), ('Michigan',        State            Team stadium_zipcode  start_point  end_point
21  Michigan  Detroit Tigers           48216         1998       1999
22  Michigan  Detroit Tigers           48201         2000       2018), ('Minnesota',         State             Team    ...     start_point  end_point
23  Minnesota  Minnesota Twins    ...            1998       2009
24  Minnesota  Minnesota Twins    ...            2010       2018

[2 rows x 5 columns]), ('Missouri',        State                 Team    ...     start_point  end_point
25  Missouri   Kansas City Royals    ...            1998       2018
26  Missouri  St. Louis Cardinals    ...            1998       2005
27  Missouri  St. Louis Cardinals    ...            2006       2018

[3 rows x 5 columns]), ('Montreal, Quebec, Canada',                        State   Team    ...     start_point  end_point
46  Montreal, Quebec, Canada  Expos    ...            1998       2004

[1 rows x 5 columns]), ('New York',        State              Team    ...     start_point  end_point
28  New York     New York Mets    ...            1998       2008
29  New York     New York Mets    ...            2009       2018
30  New York  New York Yankees    ...            1998       2008
31  New York  New York Yankees    ...            2009       2018

[4 rows x 5 columns]), ('Ohio',    State               Team stadium_zipcode  start_point  end_point
32  Ohio  Cleveland Indians           44115         1998       2018
33  Ohio    Cincinnati Reds           45202         1998       2002
34  Ohio    Cincinnati Reds           45202         2003       2018), ('Pennsylvania',            State                   Team    ...     start_point  end_point
35  Pennsylvania  Philadelphia Phillies    ...            1998       2003
36  Pennsylvania  Philadelphia Phillies    ...            2004       2018
37  Pennsylvania     Pittsburgh Pirates    ...            1998       2000
38  Pennsylvania     Pittsburgh Pirates    ...            2001       2018

[4 rows x 5 columns]), ('Texas',     State            Team stadium_zipcode  start_point  end_point
39  Texas  Houston Astros           77054         1998       1999
40  Texas  Houston Astros           77002         2000       2018
41  Texas   Texas Rangers           76011         1998       2018), ('Washington',          State              Team    ...     start_point  end_point
42  Washington  Seattle Mariners    ...            1998       1999
43  Washington  Seattle Mariners    ...            2000       2018

[2 rows x 5 columns]), ('Washington DC',             State                  Team    ...     start_point  end_point
47  Washington DC  Washington Nationals    ...            2005       2007
48  Washington DC  Washington Nationals    ...            2008       2018

[2 rows x 5 columns]), ('Wisconsin',         State               Team    ...     start_point  end_point
44  Wisconsin  Milwaukee Brewers    ...            1998       2000
45  Wisconsin  Milwaukee Brewers    ...            2001       2018

[2 rows x 5 columns])]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
['Team', 'stadium_zipcode', 'start_point', 'end_point']
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 17, in <module>
    print(list(state.Team.count))
TypeError: 'method' object is not iterable
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 16, in <module>
    ListOfStates = df_mlb.groupby('State').unique()
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 765, in __getattr__
    (type(self).__name__, attr))
AttributeError: 'DataFrameGroupBy' object has no attribute 'unique'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 17, in <module>
    TeamCount = ListOfStates.Team.count()
AttributeError: 'numpy.ndarray' object has no attribute 'Team'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 17, in <module>
    TeamCount = ListOfStates.Team.count()
AttributeError: 'numpy.ndarray' object has no attribute 'Team'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 18, in <module>
    print(list(state.Team.count()))
NameError: name 'state' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 18, in <module>
    print(list(States.state.unique()))
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 765, in __getattr__
    (type(self).__name__, attr))
AttributeError: 'DataFrameGroupBy' object has no attribute 'state'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
[('Arizona',      State                  Team    ...     start_point  end_point
0  Arizona  Arizona Diamondbacks    ...            1998       2018

[1 rows x 5 columns]), ('California',         State                  Team    ...     start_point  end_point
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004
5  California      San Diego Padres    ...            2005       2018
6  California  San Francisco Giants    ...            1998       1999
7  California  San Francisco Giants    ...            2000       2018

[7 rows x 5 columns]), ('Colorado',       State              Team stadium_zipcode  start_point  end_point
8  Colorado  Colorado Rockies           80204         1998       1994
9  Colorado  Colorado Rockies           80205         1998       2018), ('Florida',       State            Team stadium_zipcode  start_point  end_point
10  Florida   Miami Marlins           33056         1998       2011
11  Florida   Miami Marlins           33125         2012       2018
12  Florida  Tampa Bay Rays           33705         1998       2018), ('Georgia',       State            Team stadium_zipcode  start_point  end_point
13  Georgia  Atlanta Braves           30312         1998       1996
14  Georgia  Atlanta Braves           30315         1998       2016
15  Georgia  Atlanta Braves           30339         2017       2018), ('Illinois',        State               Team    ...     start_point  end_point
16  Illinois       Chicago Cubs    ...            1998       2018
17  Illinois  Chicago White Sox    ...            1998       1990
18  Illinois  Chicago White Sox    ...            1991       2018

[3 rows x 5 columns]), ('Maryland',        State               Team    ...     start_point  end_point
19  Maryland  Baltimore Orioles    ...            1998       2018

[1 rows x 5 columns]), ('Massachusetts',             State            Team    ...     start_point  end_point
20  Massachusetts  Boston Red Sox    ...            1998       2018

[1 rows x 5 columns]), ('Michigan',        State            Team stadium_zipcode  start_point  end_point
21  Michigan  Detroit Tigers           48216         1998       1999
22  Michigan  Detroit Tigers           48201         2000       2018), ('Minnesota',         State             Team    ...     start_point  end_point
23  Minnesota  Minnesota Twins    ...            1998       2009
24  Minnesota  Minnesota Twins    ...            2010       2018

[2 rows x 5 columns]), ('Missouri',        State                 Team    ...     start_point  end_point
25  Missouri   Kansas City Royals    ...            1998       2018
26  Missouri  St. Louis Cardinals    ...            1998       2005
27  Missouri  St. Louis Cardinals    ...            2006       2018

[3 rows x 5 columns]), ('Montreal, Quebec, Canada',                        State   Team    ...     start_point  end_point
46  Montreal, Quebec, Canada  Expos    ...            1998       2004

[1 rows x 5 columns]), ('New York',        State              Team    ...     start_point  end_point
28  New York     New York Mets    ...            1998       2008
29  New York     New York Mets    ...            2009       2018
30  New York  New York Yankees    ...            1998       2008
31  New York  New York Yankees    ...            2009       2018

[4 rows x 5 columns]), ('Ohio',    State               Team stadium_zipcode  start_point  end_point
32  Ohio  Cleveland Indians           44115         1998       2018
33  Ohio    Cincinnati Reds           45202         1998       2002
34  Ohio    Cincinnati Reds           45202         2003       2018), ('Pennsylvania',            State                   Team    ...     start_point  end_point
35  Pennsylvania  Philadelphia Phillies    ...            1998       2003
36  Pennsylvania  Philadelphia Phillies    ...            2004       2018
37  Pennsylvania     Pittsburgh Pirates    ...            1998       2000
38  Pennsylvania     Pittsburgh Pirates    ...            2001       2018

[4 rows x 5 columns]), ('Texas',     State            Team stadium_zipcode  start_point  end_point
39  Texas  Houston Astros           77054         1998       1999
40  Texas  Houston Astros           77002         2000       2018
41  Texas   Texas Rangers           76011         1998       2018), ('Washington',          State              Team    ...     start_point  end_point
42  Washington  Seattle Mariners    ...            1998       1999
43  Washington  Seattle Mariners    ...            2000       2018

[2 rows x 5 columns]), ('Washington DC',             State                  Team    ...     start_point  end_point
47  Washington DC  Washington Nationals    ...            2005       2007
48  Washington DC  Washington Nationals    ...            2008       2018

[2 rows x 5 columns]), ('Wisconsin',         State               Team    ...     start_point  end_point
44  Wisconsin  Milwaukee Brewers    ...            1998       2000
45  Wisconsin  Milwaukee Brewers    ...            2001       2018

[2 rows x 5 columns])]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
[('Arizona', 0    Arizona
Name: State, dtype: object), ('California', 1    California
2    California
3    California
4    California
5    California
6    California
7    California
Name: State, dtype: object), ('Colorado', 8    Colorado
9    Colorado
Name: State, dtype: object), ('Florida', 10    Florida
11    Florida
12    Florida
Name: State, dtype: object), ('Georgia', 13    Georgia
14    Georgia
15    Georgia
Name: State, dtype: object), ('Illinois', 16    Illinois
17    Illinois
18    Illinois
Name: State, dtype: object), ('Maryland', 19    Maryland
Name: State, dtype: object), ('Massachusetts', 20    Massachusetts
Name: State, dtype: object), ('Michigan', 21    Michigan
22    Michigan
Name: State, dtype: object), ('Minnesota', 23    Minnesota
24    Minnesota
Name: State, dtype: object), ('Missouri', 25    Missouri
26    Missouri
27    Missouri
Name: State, dtype: object), ('Montreal, Quebec, Canada', 46    Montreal, Quebec, Canada
Name: State, dtype: object), ('New York', 28    New York
29    New York
30    New York
31    New York
Name: State, dtype: object), ('Ohio', 32    Ohio
33    Ohio
34    Ohio
Name: State, dtype: object), ('Pennsylvania', 35    Pennsylvania
36    Pennsylvania
37    Pennsylvania
38    Pennsylvania
Name: State, dtype: object), ('Texas', 39    Texas
40    Texas
41    Texas
Name: State, dtype: object), ('Washington', 42    Washington
43    Washington
Name: State, dtype: object), ('Washington DC', 47    Washington DC
48    Washington DC
Name: State, dtype: object), ('Wisconsin', 44    Wisconsin
45    Wisconsin
Name: State, dtype: object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id GEO.display-label   ...     PAYANT     EMP
0  0400000US01           Alabama   ...     346791    7508
1  0400000US01           Alabama   ...     948747   16014
2  0400000US01           Alabama   ...    2992730   98555
3  0400000US01           Alabama   ...    9744347  284127
4  0400000US01           Alabama   ...    2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id    State NAICS.display-label   ...      RCPTOT   PAYANT     EMP
0  0400000US01  Alabama             Mining    ...     2615060   346791    7508
1  0400000US01  Alabama           Utilities   ...           Q   948747   16014
2  0400000US01  Alabama        Construction   ...    15582292  2992730   98555
3  0400000US01  Alabama       Manufacturing   ...    66686220  9744347  284127
4  0400000US01  Alabama     Wholesale trade   ...    43641369  2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 23, in <module>
    States2002 = df_mlb.groupby('State', 'Construction')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 6662, in groupby
    axis = self._get_axis_number(axis)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 375, in _get_axis_number
    .format(axis, type(self)))
ValueError: No axis named Construction for object type <class 'pandas.core.frame.DataFrame'>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id    State NAICS.display-label   ...      RCPTOT   PAYANT     EMP
0  0400000US01  Alabama             Mining    ...     2615060   346791    7508
1  0400000US01  Alabama           Utilities   ...           Q   948747   16014
2  0400000US01  Alabama        Construction   ...    15582292  2992730   98555
3  0400000US01  Alabama       Manufacturing   ...    66686220  9744347  284127
4  0400000US01  Alabama     Wholesale trade   ...    43641369  2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
<pandas.core.groupby.groupby.DataFrameGroupBy object at 0x0D6DB990>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id    State     BusinessType   ...      RCPTOT   PAYANT     EMP
0  0400000US01  Alabama          Mining    ...     2615060   346791    7508
1  0400000US01  Alabama        Utilities   ...           Q   948747   16014
2  0400000US01  Alabama     Construction   ...    15582292  2992730   98555
3  0400000US01  Alabama    Manufacturing   ...    66686220  9744347  284127
4  0400000US01  Alabama  Wholesale trade   ...    43641369  2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 24, in <module>
    print(States2002.BusinessType)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 765, in __getattr__
    (type(self).__name__, attr))
AttributeError: 'DataFrameGroupBy' object has no attribute 'BusinessType'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id    State     BusinessType   ...      RCPTOT   PAYANT     EMP
0  0400000US01  Alabama          Mining    ...     2615060   346791    7508
1  0400000US01  Alabama        Utilities   ...           Q   948747   16014
2  0400000US01  Alabama     Construction   ...    15582292  2992730   98555
3  0400000US01  Alabama    Manufacturing   ...    66686220  9744347  284127
4  0400000US01  Alabama  Wholesale trade   ...    43641369  2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 24, in <module>
    print(States2002.BusinessType)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 765, in __getattr__
    (type(self).__name__, attr))
AttributeError: 'DataFrameGroupBy' object has no attribute 'BusinessType'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id    State     BusinessType   ...      RCPTOT   PAYANT     EMP
0  0400000US01  Alabama          Mining    ...     2615060   346791    7508
1  0400000US01  Alabama        Utilities   ...           Q   948747   16014
2  0400000US01  Alabama     Construction   ...    15582292  2992730   98555
3  0400000US01  Alabama    Manufacturing   ...    66686220  9744347  284127
4  0400000US01  Alabama  Wholesale trade   ...    43641369  2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
<pandas.core.groupby.groupby.SeriesGroupBy object at 0x0D91EEB0>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id    State     BusinessType   ...      RCPTOT   PAYANT     EMP
0  0400000US01  Alabama          Mining    ...     2615060   346791    7508
1  0400000US01  Alabama        Utilities   ...           Q   948747   16014
2  0400000US01  Alabama     Construction   ...    15582292  2992730   98555
3  0400000US01  Alabama    Manufacturing   ...    66686220  9744347  284127
4  0400000US01  Alabama  Wholesale trade   ...    43641369  2661974   74915

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
State
Alabama                 [Mining , Utilities, Construction, Manufacturi...
Alaska                  [Mining , Utilities, Construction, Manufacturi...
Arizona                 [Mining , Utilities, Construction, Manufacturi...
Arkansas                [Mining , Utilities, Construction, Manufacturi...
California              [Mining , Utilities, Construction, Manufacturi...
Colorado                [Mining , Utilities, Construction, Manufacturi...
Connecticut             [Mining , Utilities, Construction, Manufacturi...
Delaware                [Mining , Utilities, Construction, Manufacturi...
District of Columbia    [Mining , Utilities, Construction, Manufacturi...
Florida                 [Mining , Utilities, Construction, Manufacturi...
Georgia                 [Mining , Utilities, Construction, Manufacturi...
Hawaii                  [Mining , Utilities, Construction, Manufacturi...
Idaho                   [Mining , Utilities, Construction, Manufacturi...
Illinois                [Mining , Utilities, Construction, Manufacturi...
Indiana                 [Mining , Utilities, Construction, Manufacturi...
Iowa                    [Mining , Utilities, Construction, Manufacturi...
Kansas                  [Mining , Utilities, Construction, Manufacturi...
Kentucky                [Mining , Utilities, Construction, Manufacturi...
Louisiana               [Mining , Utilities, Construction, Manufacturi...
Maine                   [Mining , Utilities, Construction, Manufacturi...
Maryland                [Mining , Utilities, Construction, Manufacturi...
Massachusetts           [Mining , Utilities, Construction, Manufacturi...
Michigan                [Mining , Utilities, Construction, Manufacturi...
Minnesota               [Mining , Utilities, Construction, Manufacturi...
Mississippi             [Mining , Utilities, Construction, Manufacturi...
Missouri                [Mining , Utilities, Construction, Manufacturi...
Montana                 [Mining , Utilities, Construction, Manufacturi...
Nebraska                [Mining , Utilities, Construction, Manufacturi...
Nevada                  [Mining , Utilities, Construction, Manufacturi...
New Hampshire           [Mining , Utilities, Construction, Manufacturi...
New Jersey              [Mining , Utilities, Construction, Manufacturi...
New Mexico              [Mining , Utilities, Construction, Manufacturi...
New York                [Mining , Utilities, Construction, Manufacturi...
North Carolina          [Mining , Utilities, Construction, Manufacturi...
North Dakota            [Mining , Utilities, Construction, Manufacturi...
Ohio                    [Mining , Utilities, Construction, Manufacturi...
Oklahoma                [Mining , Utilities, Construction, Manufacturi...
Oregon                  [Mining , Utilities, Construction, Manufacturi...
Pennsylvania            [Mining , Utilities, Construction, Manufacturi...
Rhode Island            [Mining , Utilities, Construction, Manufacturi...
South Carolina          [Mining , Utilities, Construction, Manufacturi...
South Dakota            [Mining , Utilities, Construction, Manufacturi...
Tennessee               [Mining , Utilities, Construction, Manufacturi...
Texas                   [Mining , Utilities, Construction, Manufacturi...
Utah                    [Mining , Utilities, Construction, Manufacturi...
Vermont                 [Mining , Utilities, Construction, Manufacturi...
Virginia                [Mining , Utilities, Construction, Manufacturi...
Washington              [Mining , Utilities, Construction, Manufacturi...
West Virginia           [Mining , Utilities, Construction, Manufacturi...
Wisconsin               [Mining , Utilities, Construction, Manufacturi...
Wyoming                 [Mining , Utilities, Construction, Manufacturi...
Name: BusinessType, dtype: object
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
State
Alabama                 [Construction]
Alaska                  [Construction]
Arizona                 [Construction]
Arkansas                [Construction]
California              [Construction]
Colorado                [Construction]
Connecticut             [Construction]
Delaware                [Construction]
District of Columbia    [Construction]
Florida                 [Construction]
Georgia                 [Construction]
Hawaii                  [Construction]
Idaho                   [Construction]
Illinois                [Construction]
Indiana                 [Construction]
Iowa                    [Construction]
Kansas                  [Construction]
Kentucky                [Construction]
Louisiana               [Construction]
Maine                   [Construction]
Maryland                [Construction]
Massachusetts           [Construction]
Michigan                [Construction]
Minnesota               [Construction]
Mississippi             [Construction]
Missouri                [Construction]
Montana                 [Construction]
Nebraska                [Construction]
Nevada                  [Construction]
New Hampshire           [Construction]
New Jersey              [Construction]
New Mexico              [Construction]
New York                [Construction]
North Carolina          [Construction]
North Dakota            [Construction]
Ohio                    [Construction]
Oklahoma                [Construction]
Oregon                  [Construction]
Pennsylvania            [Construction]
Rhode Island            [Construction]
South Carolina          [Construction]
South Dakota            [Construction]
Tennessee               [Construction]
Texas                   [Construction]
Utah                    [Construction]
Vermont                 [Construction]
Virginia                [Construction]
Washington              [Construction]
West Virginia           [Construction]
Wisconsin               [Construction]
Wyoming                 [Construction]
Name: BusinessType, dtype: object
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
<pandas.core.groupby.groupby.SeriesGroupBy object at 0x0DC10470>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
<pandas.core.groupby.groupby.SeriesGroupBy object at 0x0E520690>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
State
Alabama                  98555
Alaska                   21357
Arizona                 174871
Arkansas                 46644
California              870334
Colorado                175302
Connecticut              76594
Delaware                 25133
District of Columbia      5992
Florida                 424868
Georgia                 221292
Hawaii                   27287
Idaho                    36097
Illinois                309386
Indiana                 148230
Iowa                     67213
Kansas                   68670
Kentucky                 83946
Louisiana               123766
Maine                    30406
Maryland                181255
Massachusetts           165596
Michigan                219032
Minnesota               148430
Mississippi              49180
Missouri                153890
Montana                  22506
Nebraska                 46004
Nevada                   95253
New Hampshire            33541
New Jersey              210620
New Mexico               45282
New York                370149
North Carolina          225444
North Dakota             16864
Ohio                    257396
Oklahoma                 62684
Oregon                   87977
Pennsylvania            277400
Rhode Island             27289
South Carolina          110818
South Dakota             19040
Tennessee               123972
Texas                   555061
Utah                     67569
Vermont                  15885
Virginia                211849
Washington              167874
West Virginia            29255
Wisconsin               142230
Wyoming                  17319
Name: EMP, dtype: int64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
State
Alabama                  98555
Alaska                   21357
Arizona                 174871
Arkansas                 46644
California              870334
Colorado                175302
Connecticut              76594
Delaware                 25133
District of Columbia      5992
Florida                 424868
Georgia                 221292
Hawaii                   27287
Idaho                    36097
Illinois                309386
Indiana                 148230
Iowa                     67213
Kansas                   68670
Kentucky                 83946
Louisiana               123766
Maine                    30406
Maryland                181255
Massachusetts           165596
Michigan                219032
Minnesota               148430
Mississippi              49180
Missouri                153890
Montana                  22506
Nebraska                 46004
Nevada                   95253
New Hampshire            33541
New Jersey              210620
New Mexico               45282
New York                370149
North Carolina          225444
North Dakota             16864
Ohio                    257396
Oklahoma                 62684
Oregon                   87977
Pennsylvania            277400
Rhode Island             27289
South Carolina          110818
South Dakota             19040
Tennessee               123972
Texas                   555061
Utah                     67569
Vermont                  15885
Virginia                211849
Washington              167874
West Virginia            29255
Wisconsin               142230
Wyoming                  17319
Name: EMP, dtype: int64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
<pandas.core.groupby.groupby.SeriesGroupBy object at 0x0D8203F0>
State
Alabama                  98555
Alaska                   21357
Arizona                 174871
Arkansas                 46644
California              870334
Colorado                175302
Connecticut              76594
Delaware                 25133
District of Columbia      5992
Florida                 424868
Georgia                 221292
Hawaii                   27287
Idaho                    36097
Illinois                309386
Indiana                 148230
Iowa                     67213
Kansas                   68670
Kentucky                 83946
Louisiana               123766
Maine                    30406
Maryland                181255
Massachusetts           165596
Michigan                219032
Minnesota               148430
Mississippi              49180
Missouri                153890
Montana                  22506
Nebraska                 46004
Nevada                   95253
New Hampshire            33541
New Jersey              210620
New Mexico               45282
New York                370149
North Carolina          225444
North Dakota             16864
Ohio                    257396
Oklahoma                 62684
Oregon                   87977
Pennsylvania            277400
Rhode Island             27289
South Carolina          110818
South Dakota             19040
Tennessee               123972
Texas                   555061
Utah                     67569
Vermont                  15885
Virginia                211849
Washington              167874
West Virginia            29255
Wisconsin               142230
Wyoming                  17319
Name: EMP, dtype: int64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
State
Alabama                              [Alabama]
Alaska                                [Alaska]
Arizona                              [Arizona]
Arkansas                            [Arkansas]
California                        [California]
Colorado                            [Colorado]
Connecticut                      [Connecticut]
Delaware                            [Delaware]
District of Columbia    [District of Columbia]
Florida                              [Florida]
Georgia                              [Georgia]
Hawaii                                [Hawaii]
Idaho                                  [Idaho]
Illinois                            [Illinois]
Indiana                              [Indiana]
Iowa                                    [Iowa]
Kansas                                [Kansas]
Kentucky                            [Kentucky]
Louisiana                          [Louisiana]
Maine                                  [Maine]
Maryland                            [Maryland]
Massachusetts                  [Massachusetts]
Michigan                            [Michigan]
Minnesota                          [Minnesota]
Mississippi                      [Mississippi]
Missouri                            [Missouri]
Montana                              [Montana]
Nebraska                            [Nebraska]
Nevada                                [Nevada]
New Hampshire                  [New Hampshire]
New Jersey                        [New Jersey]
New Mexico                        [New Mexico]
New York                            [New York]
North Carolina                [North Carolina]
North Dakota                    [North Dakota]
Ohio                                    [Ohio]
Oklahoma                            [Oklahoma]
Oregon                                [Oregon]
Pennsylvania                    [Pennsylvania]
Rhode Island                    [Rhode Island]
South Carolina                [South Carolina]
South Dakota                    [South Dakota]
Tennessee                          [Tennessee]
Texas                                  [Texas]
Utah                                    [Utah]
Vermont                              [Vermont]
Virginia                            [Virginia]
Washington                        [Washington]
West Virginia                  [West Virginia]
Wisconsin                          [Wisconsin]
Wyoming                              [Wyoming]
Name: State, dtype: object
State
Alabama                  98555
Alaska                   21357
Arizona                 174871
Arkansas                 46644
California              870334
Colorado                175302
Connecticut              76594
Delaware                 25133
District of Columbia      5992
Florida                 424868
Georgia                 221292
Hawaii                   27287
Idaho                    36097
Illinois                309386
Indiana                 148230
Iowa                     67213
Kansas                   68670
Kentucky                 83946
Louisiana               123766
Maine                    30406
Maryland                181255
Massachusetts           165596
Michigan                219032
Minnesota               148430
Mississippi              49180
Missouri                153890
Montana                  22506
Nebraska                 46004
Nevada                   95253
New Hampshire            33541
New Jersey              210620
New Mexico               45282
New York                370149
North Carolina          225444
North Dakota             16864
Ohio                    257396
Oklahoma                 62684
Oregon                   87977
Pennsylvania            277400
Rhode Island             27289
South Carolina          110818
South Dakota             19040
Tennessee               123972
Texas                   555061
Utah                     67569
Vermont                  15885
Virginia                211849
Washington              167874
West Virginia            29255
Wisconsin               142230
Wyoming                  17319
Name: EMP, dtype: int64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
State
Alabama                              [Alabama]
Alaska                                [Alaska]
Arizona                              [Arizona]
Arkansas                            [Arkansas]
California                        [California]
Colorado                            [Colorado]
Connecticut                      [Connecticut]
Delaware                            [Delaware]
District of Columbia    [District of Columbia]
Florida                              [Florida]
Georgia                              [Georgia]
Hawaii                                [Hawaii]
Idaho                                  [Idaho]
Illinois                            [Illinois]
Indiana                              [Indiana]
Iowa                                    [Iowa]
Kansas                                [Kansas]
Kentucky                            [Kentucky]
Louisiana                          [Louisiana]
Maine                                  [Maine]
Maryland                            [Maryland]
Massachusetts                  [Massachusetts]
Michigan                            [Michigan]
Minnesota                          [Minnesota]
Mississippi                      [Mississippi]
Missouri                            [Missouri]
Montana                              [Montana]
Nebraska                            [Nebraska]
Nevada                                [Nevada]
New Hampshire                  [New Hampshire]
New Jersey                        [New Jersey]
New Mexico                        [New Mexico]
New York                            [New York]
North Carolina                [North Carolina]
North Dakota                    [North Dakota]
Ohio                                    [Ohio]
Oklahoma                            [Oklahoma]
Oregon                                [Oregon]
Pennsylvania                    [Pennsylvania]
Rhode Island                    [Rhode Island]
South Carolina                [South Carolina]
South Dakota                    [South Dakota]
Tennessee                          [Tennessee]
Texas                                  [Texas]
Utah                                    [Utah]
Vermont                              [Vermont]
Virginia                            [Virginia]
Washington                        [Washington]
West Virginia                  [West Virginia]
Wisconsin                          [Wisconsin]
Wyoming                              [Wyoming]
Name: State, dtype: object
State
Alabama                  98555
Alaska                   21357
Arizona                 174871
Arkansas                 46644
California              870334
Colorado                175302
Connecticut              76594
Delaware                 25133
District of Columbia      5992
Florida                 424868
Georgia                 221292
Hawaii                   27287
Idaho                    36097
Illinois                309386
Indiana                 148230
Iowa                     67213
Kansas                   68670
Kentucky                 83946
Louisiana               123766
Maine                    30406
Maryland                181255
Massachusetts           165596
Michigan                219032
Minnesota               148430
Mississippi              49180
Missouri                153890
Montana                  22506
Nebraska                 46004
Nevada                   95253
New Hampshire            33541
New Jersey              210620
New Mexico               45282
New York                370149
North Carolina          225444
North Dakota             16864
Ohio                    257396
Oklahoma                 62684
Oregon                   87977
Pennsylvania            277400
Rhode Island             27289
South Carolina          110818
South Dakota             19040
Tennessee               123972
Texas                   555061
Utah                     67569
Vermont                  15885
Virginia                211849
Washington              167874
West Virginia            29255
Wisconsin               142230
Wyoming                  17319
Name: EMP, dtype: int64
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 29, in <module>
    plt.scatter(x,y,10, c='blue', label='EMPloyement per city')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\pyplot.py", line 2864, in scatter
    is not None else {}), **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_axes.py", line 4172, in scatter
    self._process_unit_info(xdata=x, ydata=y, kwargs=kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_base.py", line 2135, in _process_unit_info
    kwargs = _process_single_axis(xdata, self.xaxis, 'xunits', kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_base.py", line 2118, in _process_single_axis
    axis.update_units(data)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axis.py", line 1473, in update_units
    default = self.converter.default_units(data, self)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 103, in default_units
    axis.set_units(UnitData(data))
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 169, in __init__
    self.update(data)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 186, in update
    for val in OrderedDict.fromkeys(data):
TypeError: unhashable type: 'numpy.ndarray'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
State
Alabama                              [Alabama]
Alaska                                [Alaska]
Arizona                              [Arizona]
Arkansas                            [Arkansas]
California                        [California]
Colorado                            [Colorado]
Connecticut                      [Connecticut]
Delaware                            [Delaware]
District of Columbia    [District of Columbia]
Florida                              [Florida]
Georgia                              [Georgia]
Hawaii                                [Hawaii]
Idaho                                  [Idaho]
Illinois                            [Illinois]
Indiana                              [Indiana]
Iowa                                    [Iowa]
Kansas                                [Kansas]
Kentucky                            [Kentucky]
Louisiana                          [Louisiana]
Maine                                  [Maine]
Maryland                            [Maryland]
Massachusetts                  [Massachusetts]
Michigan                            [Michigan]
Minnesota                          [Minnesota]
Mississippi                      [Mississippi]
Missouri                            [Missouri]
Montana                              [Montana]
Nebraska                            [Nebraska]
Nevada                                [Nevada]
New Hampshire                  [New Hampshire]
New Jersey                        [New Jersey]
New Mexico                        [New Mexico]
New York                            [New York]
North Carolina                [North Carolina]
North Dakota                    [North Dakota]
Ohio                                    [Ohio]
Oklahoma                            [Oklahoma]
Oregon                                [Oregon]
Pennsylvania                    [Pennsylvania]
Rhode Island                    [Rhode Island]
South Carolina                [South Carolina]
South Dakota                    [South Dakota]
Tennessee                          [Tennessee]
Texas                                  [Texas]
Utah                                    [Utah]
Vermont                              [Vermont]
Virginia                            [Virginia]
Washington                        [Washington]
West Virginia                  [West Virginia]
Wisconsin                          [Wisconsin]
Wyoming                              [Wyoming]
Name: State, dtype: object
State
Alabama                  98555
Alaska                   21357
Arizona                 174871
Arkansas                 46644
California              870334
Colorado                175302
Connecticut              76594
Delaware                 25133
District of Columbia      5992
Florida                 424868
Georgia                 221292
Hawaii                   27287
Idaho                    36097
Illinois                309386
Indiana                 148230
Iowa                     67213
Kansas                   68670
Kentucky                 83946
Louisiana               123766
Maine                    30406
Maryland                181255
Massachusetts           165596
Michigan                219032
Minnesota               148430
Mississippi              49180
Missouri                153890
Montana                  22506
Nebraska                 46004
Nevada                   95253
New Hampshire            33541
New Jersey              210620
New Mexico               45282
New York                370149
North Carolina          225444
North Dakota             16864
Ohio                    257396
Oklahoma                 62684
Oregon                   87977
Pennsylvania            277400
Rhode Island             27289
South Carolina          110818
South Dakota             19040
Tennessee               123972
Texas                   555061
Utah                     67569
Vermont                  15885
Virginia                211849
Washington              167874
West Virginia            29255
Wisconsin               142230
Wyoming                  17319
Name: EMP, dtype: int64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
[array(['Alabama'], dtype=object), array(['Alaska'], dtype=object), array(['Arizona'], dtype=object), array(['Arkansas'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Connecticut'], dtype=object), array(['Delaware'], dtype=object), array(['District of Columbia'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Hawaii'], dtype=object), array(['Idaho'], dtype=object), array(['Illinois'], dtype=object), array(['Indiana'], dtype=object), array(['Iowa'], dtype=object), array(['Kansas'], dtype=object), array(['Kentucky'], dtype=object), array(['Louisiana'], dtype=object), array(['Maine'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Mississippi'], dtype=object), array(['Missouri'], dtype=object), array(['Montana'], dtype=object), array(['Nebraska'], dtype=object), array(['Nevada'], dtype=object), array(['New Hampshire'], dtype=object), array(['New Jersey'], dtype=object), array(['New Mexico'], dtype=object), array(['New York'], dtype=object), array(['North Carolina'], dtype=object), array(['North Dakota'], dtype=object), array(['Ohio'], dtype=object), array(['Oklahoma'], dtype=object), array(['Oregon'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Rhode Island'], dtype=object), array(['South Carolina'], dtype=object), array(['South Dakota'], dtype=object), array(['Tennessee'], dtype=object), array(['Texas'], dtype=object), array(['Utah'], dtype=object), array(['Vermont'], dtype=object), array(['Virginia'], dtype=object), array(['Washington'], dtype=object), array(['West Virginia'], dtype=object), array(['Wisconsin'], dtype=object), array(['Wyoming'], dtype=object)]
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
[('Alabama', 0    Alabama
Name: State, dtype: object), ('Alaska', 1    Alaska
Name: State, dtype: object), ('Arizona', 2    Arizona
Name: State, dtype: object), ('Arkansas', 3    Arkansas
Name: State, dtype: object), ('California', 4    California
Name: State, dtype: object), ('Colorado', 5    Colorado
Name: State, dtype: object), ('Connecticut', 6    Connecticut
Name: State, dtype: object), ('Delaware', 7    Delaware
Name: State, dtype: object), ('District of Columbia', 8    District of Columbia
Name: State, dtype: object), ('Florida', 9    Florida
Name: State, dtype: object), ('Georgia', 10    Georgia
Name: State, dtype: object), ('Hawaii', 11    Hawaii
Name: State, dtype: object), ('Idaho', 12    Idaho
Name: State, dtype: object), ('Illinois', 13    Illinois
Name: State, dtype: object), ('Indiana', 14    Indiana
Name: State, dtype: object), ('Iowa', 15    Iowa
Name: State, dtype: object), ('Kansas', 16    Kansas
Name: State, dtype: object), ('Kentucky', 17    Kentucky
Name: State, dtype: object), ('Louisiana', 18    Louisiana
Name: State, dtype: object), ('Maine', 19    Maine
Name: State, dtype: object), ('Maryland', 20    Maryland
Name: State, dtype: object), ('Massachusetts', 21    Massachusetts
Name: State, dtype: object), ('Michigan', 22    Michigan
Name: State, dtype: object), ('Minnesota', 23    Minnesota
Name: State, dtype: object), ('Mississippi', 24    Mississippi
Name: State, dtype: object), ('Missouri', 25    Missouri
Name: State, dtype: object), ('Montana', 26    Montana
Name: State, dtype: object), ('Nebraska', 27    Nebraska
Name: State, dtype: object), ('Nevada', 28    Nevada
Name: State, dtype: object), ('New Hampshire', 29    New Hampshire
Name: State, dtype: object), ('New Jersey', 30    New Jersey
Name: State, dtype: object), ('New Mexico', 31    New Mexico
Name: State, dtype: object), ('New York', 32    New York
Name: State, dtype: object), ('North Carolina', 33    North Carolina
Name: State, dtype: object), ('North Dakota', 34    North Dakota
Name: State, dtype: object), ('Ohio', 35    Ohio
Name: State, dtype: object), ('Oklahoma', 36    Oklahoma
Name: State, dtype: object), ('Oregon', 37    Oregon
Name: State, dtype: object), ('Pennsylvania', 38    Pennsylvania
Name: State, dtype: object), ('Rhode Island', 39    Rhode Island
Name: State, dtype: object), ('South Carolina', 40    South Carolina
Name: State, dtype: object), ('South Dakota', 41    South Dakota
Name: State, dtype: object), ('Tennessee', 42    Tennessee
Name: State, dtype: object), ('Texas', 43    Texas
Name: State, dtype: object), ('Utah', 44    Utah
Name: State, dtype: object), ('Vermont', 45    Vermont
Name: State, dtype: object), ('Virginia', 46    Virginia
Name: State, dtype: object), ('Washington', 47    Washington
Name: State, dtype: object), ('West Virginia', 48    West Virginia
Name: State, dtype: object), ('Wisconsin', 49    Wisconsin
Name: State, dtype: object), ('Wyoming', 50    Wyoming
Name: State, dtype: object)]
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]

 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                    37671
1                0400000US01        ...                     8851
2                0400000US01        ...                  2074255
3                0400000US01        ...                   184866
4                0400000US01        ...                   417700

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 37, in <module>
    States2012 = df_ECN_2012.groupby('State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 6665, in groupby
    observed=observed, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 2152, in groupby
    return klass(obj, by, **kwds)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 599, in __init__
    mutated=self.mutated)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 3291, in _get_grouper
    raise KeyError(gpr)
KeyError: 'State'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 26, in <module>
    print(list(x1))
NameError: name 'x1' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 43, in <module>
    plt.scatter(x,y2,10, c='green', label='EMPloyement per city')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\pyplot.py", line 2864, in scatter
    is not None else {}), **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_axes.py", line 4182, in scatter
    raise ValueError("x and y must be the same size")
ValueError: x and y must be the same size
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
[array(['Arizona'], dtype=object), array(['California'], dtype=object), array(['Colorado'], dtype=object), array(['Florida'], dtype=object), array(['Georgia'], dtype=object), array(['Illinois'], dtype=object), array(['Maryland'], dtype=object), array(['Massachusetts'], dtype=object), array(['Michigan'], dtype=object), array(['Minnesota'], dtype=object), array(['Missouri'], dtype=object), array(['Montreal, Quebec, Canada'], dtype=object), array(['New York'], dtype=object), array(['Ohio'], dtype=object), array(['Pennsylvania'], dtype=object), array(['Texas'], dtype=object), array(['Washington'], dtype=object), array(['Washington DC'], dtype=object), array(['Wisconsin'], dtype=object)]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 19, in <module>
    plt.scatter(States,TeamCount,30, c='red', label='EMPloyement per city')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\pyplot.py", line 2864, in scatter
    is not None else {}), **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_axes.py", line 4172, in scatter
    self._process_unit_info(xdata=x, ydata=y, kwargs=kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_base.py", line 2135, in _process_unit_info
    kwargs = _process_single_axis(xdata, self.xaxis, 'xunits', kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_base.py", line 2118, in _process_single_axis
    axis.update_units(data)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axis.py", line 1473, in update_units
    default = self.converter.default_units(data, self)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 103, in default_units
    axis.set_units(UnitData(data))
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 169, in __init__
    self.update(data)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 186, in update
    for val in OrderedDict.fromkeys(data):
TypeError: unhashable type: 'numpy.ndarray'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]

 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 5, in <module>
    fig, ax = ply.subplot(nrows=2, ncols=2)
NameError: name 'ply' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 5, in <module>
    fig, ax = ply.subplots(nrows=2, ncols=2)
NameError: name 'ply' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 57, in <module>
    plt.set_rotation(45)
AttributeError: module 'matplotlib.pyplot' has no attribute 'set_rotation'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2002 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
[98555, 21357, 174871, 46644, 870334, 175302, 76594, 25133, 5992, 424868, 221292, 27287, 36097, 309386, 148230, 67213, 68670, 83946, 123766, 30406, 181255, 165596, 219032, 148430, 49180, 153890, 22506, 46004, 95253, 33541, 210620, 45282, 370149, 225444, 16864, 257396, 62684, 87977, 277400, 27289, 110818, 19040, 123972, 555061, 67569, 15885, 211849, 167874, 29255, 142230, 17319]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]

Warning (from warnings module):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 64
    result = pd.concat(frames)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=False'.

To retain the current behavior and silence the warning, pass 'sort=True'.

>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]

Warning (from warnings module):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 64
    result = pd.concat(frames)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=False'.

To retain the current behavior and silence the warning, pass 'sort=True'.

>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 64, in <module>
    result = pd.concat(df_mlb)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\concat.py", line 225, in concat
    copy=copy, sort=sort)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\concat.py", line 241, in __init__
    '"{name}"'.format(name=type(objs).__name__))
TypeError: first argument must be an iterable of pandas objects, you passed an object of type "DataFrame"
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 64, in <module>
    result = pd.concat(df_mlb,df_ECN_2012 )
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\concat.py", line 225, in concat
    copy=copy, sort=sort)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\concat.py", line 241, in __init__
    '"{name}"'.format(name=type(objs).__name__))
TypeError: first argument must be an iterable of pandas objects, you passed an object of type "DataFrame"
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 64, in <module>
    result = pd.concat(frame)
NameError: name 'frame' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]

Warning (from warnings module):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 64
    result = pd.concat(frames)
FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=False'.

To retain the current behavior and silence the warning, pass 'sort=True'.

>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
                                           State        ...        Receipts ($1,000)
0                                        Arizona        ...                      NaN
1                                     California        ...                      NaN
2                                     California        ...                      NaN
3                                     California        ...                      NaN
4                                     California        ...                      NaN
5                                     California        ...                      NaN
6                                     California        ...                      NaN
7                                     California        ...                      NaN
8                                       Colorado        ...                      NaN
9                                       Colorado        ...                      NaN
10                                       Florida        ...                      NaN
11                                       Florida        ...                      NaN
12                                       Florida        ...                      NaN
13                                       Georgia        ...                      NaN
14                                       Georgia        ...                      NaN
15                                       Georgia        ...                      NaN
16                                      Illinois        ...                      NaN
17                                      Illinois        ...                      NaN
18                                      Illinois        ...                      NaN
19                                      Maryland        ...                      NaN
20                                 Massachusetts        ...                      NaN
21                                      Michigan        ...                      NaN
22                                      Michigan        ...                      NaN
23                                     Minnesota        ...                      NaN
24                                     Minnesota        ...                      NaN
25                                      Missouri        ...                      NaN
26                                      Missouri        ...                      NaN
27                                      Missouri        ...                      NaN
28                                      New York        ...                      NaN
29                                      New York        ...                      NaN
..                                           ...        ...                      ...
26                                       Montana        ...                   616716
27                                      Nebraska        ...                   779521
28                                        Nevada        ...                   515765
29                                 New Hampshire        ...                  1140315
30                                    New Jersey        ...                  3648592
31                                    New Mexico        ...                   496358
32                                      New York        ...                  5325053
33                                North Carolina        ...                  4251393
34                                  North Dakota        ...                   333088
35                                          Ohio        ...                  4508357
36                                      Oklahoma        ...                  2226969
37                                        Oregon        ...                  1299426
38                                  Pennsylvania        ...                  5254118
39                                  Rhode Island        ...                   428960
40                                South Carolina        ...                  1956858
41                                  South Dakota        ...                   406744
42                                     Tennessee        ...                  3618277
43                                         Texas        ...                 15284366
44                                          Utah        ...                   940711
45                                       Vermont        ...                   484158
46                                      Virginia        ...                  3207108
47                                    Washington        ...                  1802478
48                                 West Virginia        ...                   383098
49                                     Wisconsin        ...                  2151978
50                                       Wyoming        ...                   237410
51                                American Samoa        ...                        N
52                                          Guam        ...                        N
53  Commonwealth of the Northern Mariana Islands        ...                        N
54                                   Puerto Rico        ...                        N
55                  United States Virgin Islands        ...                        N

[105 rows x 16 columns]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
                                             State        ...        Receipts ($1,000)
x 0                                        Arizona        ...                      NaN
  1                                     California        ...                      NaN
  2                                     California        ...                      NaN
  3                                     California        ...                      NaN
  4                                     California        ...                      NaN
  5                                     California        ...                      NaN
  6                                     California        ...                      NaN
  7                                     California        ...                      NaN
  8                                       Colorado        ...                      NaN
  9                                       Colorado        ...                      NaN
  10                                       Florida        ...                      NaN
  11                                       Florida        ...                      NaN
  12                                       Florida        ...                      NaN
  13                                       Georgia        ...                      NaN
  14                                       Georgia        ...                      NaN
  15                                       Georgia        ...                      NaN
  16                                      Illinois        ...                      NaN
  17                                      Illinois        ...                      NaN
  18                                      Illinois        ...                      NaN
  19                                      Maryland        ...                      NaN
  20                                 Massachusetts        ...                      NaN
  21                                      Michigan        ...                      NaN
  22                                      Michigan        ...                      NaN
  23                                     Minnesota        ...                      NaN
  24                                     Minnesota        ...                      NaN
  25                                      Missouri        ...                      NaN
  26                                      Missouri        ...                      NaN
  27                                      Missouri        ...                      NaN
  28                                      New York        ...                      NaN
  29                                      New York        ...                      NaN
...                                            ...        ...                      ...
y 26                                       Montana        ...                   616716
  27                                      Nebraska        ...                   779521
  28                                        Nevada        ...                   515765
  29                                 New Hampshire        ...                  1140315
  30                                    New Jersey        ...                  3648592
  31                                    New Mexico        ...                   496358
  32                                      New York        ...                  5325053
  33                                North Carolina        ...                  4251393
  34                                  North Dakota        ...                   333088
  35                                          Ohio        ...                  4508357
  36                                      Oklahoma        ...                  2226969
  37                                        Oregon        ...                  1299426
  38                                  Pennsylvania        ...                  5254118
  39                                  Rhode Island        ...                   428960
  40                                South Carolina        ...                  1956858
  41                                  South Dakota        ...                   406744
  42                                     Tennessee        ...                  3618277
  43                                         Texas        ...                 15284366
  44                                          Utah        ...                   940711
  45                                       Vermont        ...                   484158
  46                                      Virginia        ...                  3207108
  47                                    Washington        ...                  1802478
  48                                 West Virginia        ...                   383098
  49                                     Wisconsin        ...                  2151978
  50                                       Wyoming        ...                   237410
  51                                American Samoa        ...                        N
  52                                          Guam        ...                        N
  53  Commonwealth of the Northern Mariana Islands        ...                        N
  54                                   Puerto Rico        ...                        N
  55                  United States Virgin Islands        ...                        N

[105 rows x 16 columns]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
                                           State        ...        Receipts ($1,000)
0                                        Alabama        ...                  2074255
1                                         Alaska        ...                   259663
2                                        Arizona        ...                  1771113
3                                       Arkansas        ...                  1470235
4                                     California        ...                 11552985
5                                       Colorado        ...                  2803092
6                                    Connecticut        ...                  2530959
7                                       Delaware        ...                   387216
8                           District of Columbia        ...                    98391
9                                        Florida        ...                  7213211
10                                       Georgia        ...                  4632779
11                                        Hawaii        ...                   457014
12                                         Idaho        ...                   655767
13                                      Illinois        ...                  4369757
14                                       Indiana        ...                  2308032
15                                          Iowa        ...                  1478199
16                                        Kansas        ...                  1051393
17                                      Kentucky        ...                  1904651
18                                     Louisiana        ...                  2129709
19                                         Maine        ...                   846586
20                                      Maryland        ...                  2268044
21                                 Massachusetts        ...                  3882960
22                                      Michigan        ...                  3580578
23                                     Minnesota        ...                  2266945
24                                   Mississippi        ...                  1322116
25                                      Missouri        ...                  2435652
26                                       Montana        ...                   616716
27                                      Nebraska        ...                   779521
28                                        Nevada        ...                   515765
29                                 New Hampshire        ...                  1140315
30                                    New Jersey        ...                  3648592
31                                    New Mexico        ...                   496358
32                                      New York        ...                  5325053
33                                North Carolina        ...                  4251393
34                                  North Dakota        ...                   333088
35                                          Ohio        ...                  4508357
36                                      Oklahoma        ...                  2226969
37                                        Oregon        ...                  1299426
38                                  Pennsylvania        ...                  5254118
39                                  Rhode Island        ...                   428960
40                                South Carolina        ...                  1956858
41                                  South Dakota        ...                   406744
42                                     Tennessee        ...                  3618277
43                                         Texas        ...                 15284366
44                                          Utah        ...                   940711
45                                       Vermont        ...                   484158
46                                      Virginia        ...                  3207108
47                                    Washington        ...                  1802478
48                                 West Virginia        ...                   383098
49                                     Wisconsin        ...                  2151978
50                                       Wyoming        ...                   237410
51                                American Samoa        ...                        N
52                                          Guam        ...                        N
53  Commonwealth of the Northern Mariana Islands        ...                        N
54                                   Puerto Rico        ...                        N
55                  United States Virgin Islands        ...                        N

[56 rows x 16 columns]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
0      78690.0
1      24196.0
2     123886.0
3      42999.0
4     597265.0
5     123511.0
6      55906.0
7      17774.0
8       9014.0
9     294737.0
10    144980.0
11     27672.0
12     32060.0
13    204850.0
14    123907.0
15     66013.0
16     58819.0
17     64026.0
18    136437.0
19     25391.0
20    144153.0
21    120749.0
22    131793.0
23    113683.0
24     41541.0
25    110373.0
26     23980.0
27     40543.0
28     54569.0
29     24435.0
30    147059.0
31     37787.0
32    333892.0
33    180605.0
34     25823.0
35    181218.0
36     69690.0
37     69777.0
38    238226.0
39     17501.0
40     68701.0
41     19795.0
42    101770.0
43    573225.0
44     64516.0
45     15816.0
46    177109.0
47    138671.0
48     26653.0
49    102538.0
50     21300.0
51       432.0
52      6722.0
53       821.0
54     36814.0
55      1729.0
Name: EMP, dtype: float64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
0                                          Alabama
1                                           Alaska
2                                          Arizona
3                                         Arkansas
4                                       California
5                                         Colorado
6                                      Connecticut
7                                         Delaware
8                             District of Columbia
9                                          Florida
10                                         Georgia
11                                          Hawaii
12                                           Idaho
13                                        Illinois
14                                         Indiana
15                                            Iowa
16                                          Kansas
17                                        Kentucky
18                                       Louisiana
19                                           Maine
20                                        Maryland
21                                   Massachusetts
22                                        Michigan
23                                       Minnesota
24                                     Mississippi
25                                        Missouri
26                                         Montana
27                                        Nebraska
28                                          Nevada
29                                   New Hampshire
30                                      New Jersey
31                                      New Mexico
32                                        New York
33                                  North Carolina
34                                    North Dakota
35                                            Ohio
36                                        Oklahoma
37                                          Oregon
38                                    Pennsylvania
39                                    Rhode Island
40                                  South Carolina
41                                    South Dakota
42                                       Tennessee
43                                           Texas
44                                            Utah
45                                         Vermont
46                                        Virginia
47                                      Washington
48                                   West Virginia
49                                       Wisconsin
50                                         Wyoming
51                                  American Samoa
52                                            Guam
53    Commonwealth of the Northern Mariana Islands
54                                     Puerto Rico
55                    United States Virgin Islands
Name: State, dtype: object 0      78690.0
1      24196.0
2     123886.0
3      42999.0
4     597265.0
5     123511.0
6      55906.0
7      17774.0
8       9014.0
9     294737.0
10    144980.0
11     27672.0
12     32060.0
13    204850.0
14    123907.0
15     66013.0
16     58819.0
17     64026.0
18    136437.0
19     25391.0
20    144153.0
21    120749.0
22    131793.0
23    113683.0
24     41541.0
25    110373.0
26     23980.0
27     40543.0
28     54569.0
29     24435.0
30    147059.0
31     37787.0
32    333892.0
33    180605.0
34     25823.0
35    181218.0
36     69690.0
37     69777.0
38    238226.0
39     17501.0
40     68701.0
41     19795.0
42    101770.0
43    573225.0
44     64516.0
45     15816.0
46    177109.0
47    138671.0
48     26653.0
49    102538.0
50     21300.0
51       432.0
52      6722.0
53       821.0
54     36814.0
55      1729.0
Name: EMP, dtype: float64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 66, in <module>
    print (ist (result.loc['y']))
NameError: name 'ist' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 66, in <module>
    print (ist (result))
NameError: name 'ist' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 66, in <module>
    print (iist (result.loc['y']))
NameError: name 'iist' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 66, in <module>
    print (iist (result))
NameError: name 'iist' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
                                             State        ...        Receipts ($1,000)
x 0                                        Arizona        ...                      NaN
  1                                     California        ...                      NaN
  2                                     California        ...                      NaN
  3                                     California        ...                      NaN
  4                                     California        ...                      NaN
  5                                     California        ...                      NaN
  6                                     California        ...                      NaN
  7                                     California        ...                      NaN
  8                                       Colorado        ...                      NaN
  9                                       Colorado        ...                      NaN
  10                                       Florida        ...                      NaN
  11                                       Florida        ...                      NaN
  12                                       Florida        ...                      NaN
  13                                       Georgia        ...                      NaN
  14                                       Georgia        ...                      NaN
  15                                       Georgia        ...                      NaN
  16                                      Illinois        ...                      NaN
  17                                      Illinois        ...                      NaN
  18                                      Illinois        ...                      NaN
  19                                      Maryland        ...                      NaN
  20                                 Massachusetts        ...                      NaN
  21                                      Michigan        ...                      NaN
  22                                      Michigan        ...                      NaN
  23                                     Minnesota        ...                      NaN
  24                                     Minnesota        ...                      NaN
  25                                      Missouri        ...                      NaN
  26                                      Missouri        ...                      NaN
  27                                      Missouri        ...                      NaN
  28                                      New York        ...                      NaN
  29                                      New York        ...                      NaN
...                                            ...        ...                      ...
y 26                                       Montana        ...                   616716
  27                                      Nebraska        ...                   779521
  28                                        Nevada        ...                   515765
  29                                 New Hampshire        ...                  1140315
  30                                    New Jersey        ...                  3648592
  31                                    New Mexico        ...                   496358
  32                                      New York        ...                  5325053
  33                                North Carolina        ...                  4251393
  34                                  North Dakota        ...                   333088
  35                                          Ohio        ...                  4508357
  36                                      Oklahoma        ...                  2226969
  37                                        Oregon        ...                  1299426
  38                                  Pennsylvania        ...                  5254118
  39                                  Rhode Island        ...                   428960
  40                                South Carolina        ...                  1956858
  41                                  South Dakota        ...                   406744
  42                                     Tennessee        ...                  3618277
  43                                         Texas        ...                 15284366
  44                                          Utah        ...                   940711
  45                                       Vermont        ...                   484158
  46                                      Virginia        ...                  3207108
  47                                    Washington        ...                  1802478
  48                                 West Virginia        ...                   383098
  49                                     Wisconsin        ...                  2151978
  50                                       Wyoming        ...                   237410
  51                                American Samoa        ...                        N
  52                                          Guam        ...                        N
  53  Commonwealth of the Northern Mariana Islands        ...                        N
  54                                   Puerto Rico        ...                        N
  55                  United States Virgin Islands        ...                        N

[105 rows x 16 columns]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
105
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
x  0                                          Arizona
   1                                       California
   2                                       California
   3                                       California
   4                                       California
   5                                       California
   6                                       California
   7                                       California
   8                                         Colorado
   9                                         Colorado
   10                                         Florida
   11                                         Florida
   12                                         Florida
   13                                         Georgia
   14                                         Georgia
   15                                         Georgia
   16                                        Illinois
   17                                        Illinois
   18                                        Illinois
   19                                        Maryland
   20                                   Massachusetts
   21                                        Michigan
   22                                        Michigan
   23                                       Minnesota
   24                                       Minnesota
   25                                        Missouri
   26                                        Missouri
   27                                        Missouri
   28                                        New York
   29                                        New York
                             ...                     
y  26                                         Montana
   27                                        Nebraska
   28                                          Nevada
   29                                   New Hampshire
   30                                      New Jersey
   31                                      New Mexico
   32                                        New York
   33                                  North Carolina
   34                                    North Dakota
   35                                            Ohio
   36                                        Oklahoma
   37                                          Oregon
   38                                    Pennsylvania
   39                                    Rhode Island
   40                                  South Carolina
   41                                    South Dakota
   42                                       Tennessee
   43                                           Texas
   44                                            Utah
   45                                         Vermont
   46                                        Virginia
   47                                      Washington
   48                                   West Virginia
   49                                       Wisconsin
   50                                         Wyoming
   51                                  American Samoa
   52                                            Guam
   53    Commonwealth of the Northern Mariana Islands
   54                                     Puerto Rico
   55                    United States Virgin Islands
Name: State, Length: 105, dtype: object
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 66, in <module>
    print (result.State.EMP)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'EMP'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 64, in <module>
    result = pd.concat(frames, sort=False, on='State')
TypeError: concat() got an unexpected keyword argument 'on'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
            State        ...        Receipts ($1,000)
0         Arizona        ...                  1771113
1      California        ...                 11552985
2      California        ...                 11552985
3      California        ...                 11552985
4      California        ...                 11552985
5      California        ...                 11552985
6      California        ...                 11552985
7      California        ...                 11552985
8        Colorado        ...                  2803092
9        Colorado        ...                  2803092
10        Florida        ...                  7213211
11        Florida        ...                  7213211
12        Florida        ...                  7213211
13        Georgia        ...                  4632779
14        Georgia        ...                  4632779
15        Georgia        ...                  4632779
16       Illinois        ...                  4369757
17       Illinois        ...                  4369757
18       Illinois        ...                  4369757
19       Maryland        ...                  2268044
20  Massachusetts        ...                  3882960
21       Michigan        ...                  3580578
22       Michigan        ...                  3580578
23      Minnesota        ...                  2266945
24      Minnesota        ...                  2266945
25       Missouri        ...                  2435652
26       Missouri        ...                  2435652
27       Missouri        ...                  2435652
28       New York        ...                  5325053
29       New York        ...                  5325053
30       New York        ...                  5325053
31       New York        ...                  5325053
32           Ohio        ...                  4508357
33           Ohio        ...                  4508357
34           Ohio        ...                  4508357
35   Pennsylvania        ...                  5254118
36   Pennsylvania        ...                  5254118
37   Pennsylvania        ...                  5254118
38   Pennsylvania        ...                  5254118
39          Texas        ...                 15284366
40          Texas        ...                 15284366
41          Texas        ...                 15284366
42     Washington        ...                  1802478
43     Washington        ...                  1802478
44      Wisconsin        ...                  2151978
45      Wisconsin        ...                  2151978

[46 rows x 16 columns]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 67, in <module>
    print (result.groupby('SState'))
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\generic.py", line 6665, in groupby
    observed=observed, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 2152, in groupby
    return klass(obj, by, **kwds)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 599, in __init__
    mutated=self.mutated)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 3291, in _get_grouper
    raise KeyError(gpr)
KeyError: 'SState'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
<pandas.core.groupby.groupby.DataFrameGroupBy object at 0x0FC289D0>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
               Team        ...          Receipts ($1,000)
State                      ...                           
Arizona           1        ...                          1
California        7        ...                          7
Colorado          2        ...                          2
Florida           3        ...                          3
Georgia           3        ...                          3
Illinois          3        ...                          3
Maryland          1        ...                          1
Massachusetts     1        ...                          1
Michigan          2        ...                          2
Minnesota         2        ...                          2
Missouri          3        ...                          3
New York          4        ...                          4
Ohio              3        ...                          3
Pennsylvania      4        ...                          4
Texas             3        ...                          3
Washington        2        ...                          2
Wisconsin         2        ...                          2

[17 rows x 15 columns]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
<pandas.core.groupby.groupby.SeriesGroupBy object at 0x0FC3B550>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
State
Arizona           123886
California       4180855
Colorado          247022
Florida           884211
Georgia           434940
Illinois          614550
Maryland          144153
Massachusetts     120749
Michigan          263586
Minnesota         227366
Missouri          331119
New York         1335568
Ohio              543654
Pennsylvania      952904
Texas            1719675
Washington        277342
Wisconsin         205076
Name: EMP, dtype: int64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
State
Arizona           123886
California       4180855
Colorado          247022
Florida           884211
Georgia           434940
Illinois          614550
Maryland          144153
Massachusetts     120749
Michigan          263586
Minnesota         227366
Missouri          331119
New York         1335568
Ohio              543654
Pennsylvania      952904
Texas            1719675
Washington        277342
Wisconsin         205076
Name: EMP, dtype: int64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
               Team        ...          Receipts ($1,000)
State                      ...                           
Arizona           1        ...                          1
California        7        ...                          7
Colorado          2        ...                          2
Florida           3        ...                          3
Georgia           3        ...                          3
Illinois          3        ...                          3
Maryland          1        ...                          1
Massachusetts     1        ...                          1
Michigan          2        ...                          2
Minnesota         2        ...                          2
Missouri          3        ...                          3
New York          4        ...                          4
Ohio              3        ...                          3
Pennsylvania      4        ...                          4
Texas             3        ...                          3
Washington        2        ...                          2
Wisconsin         2        ...                          2

[17 rows x 15 columns]
State
Arizona           123886
California       4180855
Colorado          247022
Florida           884211
Georgia           434940
Illinois          614550
Maryland          144153
Massachusetts     120749
Michigan          263586
Minnesota         227366
Missouri          331119
New York         1335568
Ohio              543654
Pennsylvania      952904
Texas            1719675
Washington        277342
Wisconsin         205076
Name: EMP, dtype: int64
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
               Team        ...          Receipts ($1,000)
State                      ...                           
Arizona           1        ...                          1
California        7        ...                          7
Colorado          2        ...                          2
Florida           3        ...                          3
Georgia           3        ...                          3
Illinois          3        ...                          3
Maryland          1        ...                          1
Massachusetts     1        ...                          1
Michigan          2        ...                          2
Minnesota         2        ...                          2
Missouri          3        ...                          3
New York          4        ...                          4
Ohio              3        ...                          3
Pennsylvania      4        ...                          4
Texas             3        ...                          3
Washington        2        ...                          2
Wisconsin         2        ...                          2

[17 rows x 15 columns]
State
Arizona           123886
California       4180855
Colorado          247022
Florida           884211
Georgia           434940
Illinois          614550
Maryland          144153
Massachusetts     120749
Michigan          263586
Minnesota         227366
Missouri          331119
New York         1335568
Ohio              543654
Pennsylvania      952904
Texas            1719675
Washington        277342
Wisconsin         205076
Name: EMP, dtype: int64
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 71, in <module>
    newresult = pd.merge (myList, myEmpList, on ='State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\merge.py", line 61, in merge
    validate=validate)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\merge.py", line 527, in __init__
    'type {right}'.format(right=type(right)))
ValueError: can not merge DataFrame with instance of type <class 'pandas.core.series.Series'>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
State
Arizona          1
California       7
Colorado         2
Florida          3
Georgia          3
Illinois         3
Maryland         1
Massachusetts    1
Michigan         2
Minnesota        2
Missouri         3
New York         4
Ohio             3
Pennsylvania     4
Texas            3
Washington       2
Wisconsin        2
Name: Team, dtype: int64
State
Arizona           123886
California       4180855
Colorado          247022
Florida           884211
Georgia           434940
Illinois          614550
Maryland          144153
Massachusetts     120749
Michigan          263586
Minnesota         227366
Missouri          331119
New York         1335568
Ohio              543654
Pennsylvania      952904
Texas            1719675
Washington        277342
Wisconsin         205076
Name: EMP, dtype: int64
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 71, in <module>
    newresult = pd.merge (myList, myEmpList, on ='State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\merge.py", line 61, in merge
    validate=validate)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\merge.py", line 524, in __init__
    'type {left}'.format(left=type(left)))
ValueError: can not merge DataFrame with instance of type <class 'pandas.core.series.Series'>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
17
17
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 71, in <module>
    newresult = pd.merge (myList, myEmpList, on ='State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\merge.py", line 61, in merge
    validate=validate)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\reshape\merge.py", line 524, in __init__
    'type {left}'.format(left=type(left)))
ValueError: can not merge DataFrame with instance of type <class 'pandas.core.series.Series'>
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 69, in <module>
    print(myList.size())
TypeError: 'int' object is not callable
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
17
17
123886.0
597265.0
123511.0
294737.0
144980.0
204850.0
144153.0
120749.0
131793.0
113683.0
110373.0
333892.0
181218.0
238226.0
573225.0
138671.0
102538.0
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin']
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 76, in <module>
    print(list(y3))
TypeError: 'numpy.float64' object is not iterable
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 4, 3, 4, 3, 2, 2]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 76, in <module>
    print(list(y3))
TypeError: 'numpy.float64' object is not iterable
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
State
Arizona          1
California       7
Colorado         2
Florida          3
Georgia          3
Illinois         3
Maryland         1
Massachusetts    1
Michigan         2
Minnesota        2
Missouri         3
New York         4
Ohio             3
Pennsylvania     4
Texas            3
Washington       2
Wisconsin        2
Name: Team, dtype: int64
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 76, in <module>
    print(list(y3))
TypeError: 'numpy.float64' object is not iterable
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
State
Arizona          1
California       7
Colorado         2
Florida          3
Georgia          3
Illinois         3
Maryland         1
Massachusetts    1
Michigan         2
Minnesota        2
Missouri         3
New York         4
Ohio             3
Pennsylvania     4
Texas            3
Washington       2
Wisconsin        2
Name: Team, dtype: int64
102538.0
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 79, in <module>
    plt.scatter(x3,y3,20, c='green', label='2012 - EMPloyement per State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\pyplot.py", line 2864, in scatter
    is not None else {}), **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_axes.py", line 4182, in scatter
    raise ValueError("x and y must be the same size")
ValueError: x and y must be the same size
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
17
1
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 79, in <module>
    plt.scatter(x3,y3,20, c='green', label='2012 - EMPloyement per State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\pyplot.py", line 2864, in scatter
    is not None else {}), **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_axes.py", line 4182, in scatter
    raise ValueError("x and y must be the same size")
ValueError: x and y must be the same size
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
17
102538.0
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 79, in <module>
    plt.scatter(x3,y3,20, c='green', label='2012 - EMPloyement per State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\pyplot.py", line 2864, in scatter
    is not None else {}), **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_axes.py", line 4182, in scatter
    raise ValueError("x and y must be the same size")
ValueError: x and y must be the same size
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 70, in <module>
    myEmploymentperTeamRatio[index] = (myEmpList[index]/myList[index])
NameError: name 'myEmploymentperTeamRatio' is not defined
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
17
[123886.0, 597265.0, 123511.0, 294737.0, 144980.0, 204850.0, 144153.0, 120749.0, 131793.0, 113683.0, 110373.0, 333892.0, 181218.0, 238226.0, 573225.0, 138671.0, 102538.0]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
17
[123886.0, 597265.0, 123511.0, 294737.0, 144980.0, 204850.0, 144153.0, 120749.0, 131793.0, 113683.0, 110373.0, 333892.0, 181218.0, 238226.0, 573225.0, 138671.0, 102538.0]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
<pandas.core.groupby.groupby.SeriesGroupBy object at 0x0FBA79B0>
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 77, in <module>
    plt.scatter(x3,y3,20, c='green', label='Employment/Team by State')
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\pyplot.py", line 2864, in scatter
    is not None else {}), **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_axes.py", line 4172, in scatter
    self._process_unit_info(xdata=x, ydata=y, kwargs=kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_base.py", line 2135, in _process_unit_info
    kwargs = _process_single_axis(xdata, self.xaxis, 'xunits', kwargs)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axes\_base.py", line 2118, in _process_single_axis
    axis.update_units(data)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\axis.py", line 1473, in update_units
    default = self.converter.default_units(data, self)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 103, in default_units
    axis.set_units(UnitData(data))
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 169, in __init__
    self.update(data)
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\matplotlib\category.py", line 186, in update
    for val in OrderedDict.fromkeys(data):
TypeError: unhashable type: 'numpy.ndarray'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
Traceback (most recent call last):
  File "C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py", line 72, in <module>
    x3 = result.groupby('State').unique()
  File "C:\Users\scott\AppData\Roaming\Python\Python37\site-packages\pandas\core\groupby\groupby.py", line 765, in __getattr__
    (type(self).__name__, attr))
AttributeError: 'DataFrameGroupBy' object has no attribute 'unique'
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
['Arizona' 'California' 'Colorado' 'Florida' 'Georgia' 'Illinois'
 'Maryland' 'Massachusetts' 'Michigan' 'Minnesota' 'Missouri' 'New York'
 'Ohio' 'Pennsylvania' 'Texas' 'Washington' 'Wisconsin']
>>> 
 RESTART: C:\Users\scott\Desktop\vazi work in progress\Python Homework\Project\sports.py 
        State                  Team    ...     start_point  end_point
0     Arizona  Arizona Diamondbacks    ...            1998       2018
1  California    Los Angeles Angels    ...            1998       2018
2  California   Los Angeles Dodgers    ...            1998       2018
3  California           Oakland A's    ...            1998       2018
4  California      San Diego Padres    ...            1998       2004

[5 rows x 5 columns]
        GEO.id       State  BusinessType   ...       RCPTOT    PAYANT     EMP
0  0400000US01     Alabama  Construction   ...     15582292   2992730   98555
1  0400000US02      Alaska  Construction   ...      4417369    938457   21357
2  0400000US04     Arizona  Construction   ...     28926214   5628936  174871
3  0400000US05    Arkansas  Construction   ...      6623949   1297957   46644
4  0400000US06  California  Construction   ...    150527556  32986608  870334

[5 rows x 9 columns]
  Geographic identifier code        ...        Receipts ($1,000)
0                0400000US01        ...                  2074255
1                0400000US02        ...                   259663
2                0400000US04        ...                  1771113
3                0400000US05        ...                  1470235
4                0400000US06        ...                 11552985

[5 rows x 12 columns]
State and number of teams
['Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Missouri', 'New York', 'Ohio', 'Pennsylvania', 'Texas', 'Washington', 'Wisconsin', 'Montreal, Quebec, Canada', 'Washington DC']
[1, 7, 2, 3, 3, 3, 1, 1, 2, 2, 3, 1, 4, 3, 4, 3, 2, 2, 2]
2012 - Number of business established, Annual Payroll & Number of Employees
['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'American Samoa', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'Puerto Rico', 'United States Virgin Islands']
[78690, 24196, 432, 123886, 42999, 597265, 123511, 821, 55906, 17774, 9014, 294737, 144980, 6722, 27672, 32060, 204850, 123907, 66013, 58819, 64026, 136437, 25391, 144153, 120749, 131793, 113683, 41541, 110373, 23980, 40543, 54569, 24435, 147059, 37787, 333892, 180605, 25823, 181218, 69690, 69777, 238226, 36814, 17501, 68701, 19795, 101770, 573225, 1729, 64516, 15816, 177109, 138671, 26653, 102538, 21300]
