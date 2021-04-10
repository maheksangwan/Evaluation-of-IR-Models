{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "# if you are using python 3, you should \n",
    "import urllib.request\n",
    "from urllib.parse import quote\n",
    "#import urllib2\n",
    "\n",
    "IRModel='BM25' #change value to vsm for the other model\n",
    "\n",
    "\n",
    "lines = [line.rstrip('\\n') for line in open('test-queries.txt',encoding='utf-8')]\n",
    "i=1\n",
    "for line in lines:\n",
    "    \n",
    "    qid,query = line.split(maxsplit=1)\n",
    "    query = query.replace(':','\\:')\n",
    "    query = quote(query)\n",
    "    query = query.replace(' ','%20')\n",
    "\n",
    "    # for vsm change the qid, name of core and IR Model\n",
    "    inurl = 'http://100.26.225.121:8984/solr/IRF20P3_VSM/select?defType=dismax&fl=id,%20score&indent=on&q='+str(query)+'&qf=tweet_hashtags^3%20text_en^6%20text_ru^6%20text_de^6%20text_en_copy%20text_de_copy%20text_ru_copy&rows=20&wt=json'\n",
    "    outf = str(i)+'.txt'\n",
    "    out = open(outf, 'w')\n",
    "    #data = urllib2.urlopen(inurl)\n",
    "    # if you're using python 3, you should use\n",
    "    data = urllib.request.urlopen(inurl)\n",
    "    docs = json.load(data)['response']['docs']\n",
    "    \n",
    "    # the ranking should start from 1 and increase\n",
    "    count = 1\n",
    "    for doc in docs:\n",
    "        #print(doc)\n",
    "        out.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\\n')\n",
    "        count += 1\n",
    "    out.close()\n",
    "    i+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
