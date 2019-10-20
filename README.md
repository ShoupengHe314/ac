# acPDRP
acPDRP, a predictor of multiple features in protein disordered regions ,was trained by Uniprot90 and tested by CASP9 and CASP10 datasets.
The results of four evaluation indexes including Precision, Bacc, MCC and AUC in two datasets of CASP9 and CASP10 are better than DeepCNF-D and the related methods mentioned.



## News
- 18/10/2019: Upload the script and the predicted model for the first time and test if it is available


## Get started


### Environment Requires

- Anaconda 3.7


### Install
Download and install Anaconda 3.7, and import acpdrp.py into the installed Anaconda path:Anaconda3\Lib\site-packages.


### Using
You can python the script called predict_test.py and the input file is your protein sequence the output files are the predicted results.

```
python predict_test.py <Input File> <Output Files>
```


### Input Files
The input file must be a protein sequence and format in FASTA.  
In view of the protein sequence requirements of DISPHOS1.3 for protein phosphorylation site prediction,  
the minimal length of the protein sequence is limited to 25 residues and the maximal one is limited to 5000 residues.  
The FASTA sequence seems like below:
```
>test_sequence
IMWRNAKRQSDRFYDEDVFINGEGLEPEQDTRGVDNAHMVTNHHALRSRDNIYEYRDSPSTKTLASKAHTDTTSLRSPSSLAMTQKSSSQASLKSGISLKETNGHLVKQSERAATPRSQQNGSIAKVASPPVEEKRLLQPLSSTPVTQLQAEPAKRVPTAASVSGSSRSTTPVPSARSTTTHTTTATLSSQPAAQPRRTHLVEGVPQTSVHHHHHH
```

### Output Files
The first line is sequence name.and the second line is predicted score.  
The time-consuming of getting the prediction results is related to the length of the input protein sequence.  
The longer the length is, the longer the time-consuming is.  
The output file seems like below:

```
>test_sequence
0.0230,00554

```

## References
Wu C , Chen J , Liu Y , et al. Improved Prediction of Regulatory Element Using Hybrid Abelian Complexity Features with DNA Sequences[J]. International Journal of Molecular Sciences, 2019, 20(7).

Wang, Sheng, Weng, et al. IJMS, Vol. 16, Pages 17315-17330: DeepCNF-D: Predicting Protein Order/Disorder Regions by Weighted Deep Convolutional Neural Fields[J]. 2015.

Iakoucheva LM, Radivojac P, Brown CJ, O'Connor TR, Sikes JG, Obradovic Z, Dunker AK. Intrinsic disorder and protein phosphorylation. Nucleic Acids Research, 2004, 32 (3), 1037-1049.
