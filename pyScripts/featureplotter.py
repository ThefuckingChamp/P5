import linreg
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import pearsonr

# style.use('ggplot')


data = pd.read_csv('C:/P5GIT/featurized_ch1_period_testing.csv', sep = ';', encoding = 'utf-8')



features = [
			# 'size_scale',
			# 'discount_pct',
			# 'price',
			# 'style_age_chain',
			# 'total_turnover_chain_rolling',
			# 'total_quantity_chain_rolling',
			# 'qty_p1_chain_prod_rolling_7',
			# 'qty_p2_chain_prod_rolling_7',
			# 'qty_p3_chain_prod_rolling_7',
			# # 'avg_price_chain',
			# 'style_age_ret',
			# 'total_turnover_ret_rolling_7',
			# 'total_quantity_ret_rolling_7',
			 # 'avg_price_ret',
			'qty_p1_ret_prod_rolling_7',
			'qty_p2_ret_prod_rolling_7',
			'qty_p3_ret_prod_rolling_7',
			'qty_speed_ret_prod_p1p2_rolling_7',
    		'qty_speed_ret_prod_p2p3_rolling_7',
    		'qty_acc_ret_prod_p1p3_rolling_7', 
    		'qty_p1_ret_prod_rolling_3',
			'qty_p2_ret_prod_rolling_3',
			'qty_p3_ret_prod_rolling_3',
			'qty_speed_ret_prod_p1p2_rolling_3',
    		'qty_speed_ret_prod_p2p3_rolling_3',
    		'qty_acc_ret_prod_p1p3_rolling_3', 
    		'qty_p1_ret_prod_rolling_1',
			'qty_p2_ret_prod_rolling_1',
			'qty_p3_ret_prod_rolling_1',
			'qty_speed_ret_prod_p1p2_rolling_1',
    		'qty_speed_ret_prod_p2p3_rolling_1',
    		'qty_acc_ret_prod_p1p3_rolling_1',

    		'qty_p1_ret_style_rolling_7',
			'qty_p2_ret_style_rolling_7',
			'qty_p3_ret_style_rolling_7',
			# 'qty_speed_ret_style_p1p2_rolling_7',
    		# 'qty_speed_ret_style_p2p3_rolling_7',
    		# 'qty_acc_ret_style_p1p3_rolling_7', 
    		'qty_p1_ret_style_rolling_3',
			'qty_p2_ret_style_rolling_3',
			'qty_p3_ret_style_rolling_3',
			# 'qty_speed_ret_style_p1p2_rolling_3',
   #  		'qty_speed_ret_style_p2p3_rolling_3',
    		# 'qty_acc_ret_style_p1p3_rolling_3', 
    		'qty_p1_ret_style_rolling_1',
			'qty_p2_ret_style_rolling_1',
			'qty_p3_ret_style_rolling_1'#,
			# 'qty_speed_ret_style_p1p2_rolling_1',
   #  		'qty_speed_ret_style_p2p3_rolling_1',
   #  		'qty_acc_ret_style_p1p3_rolling_1' 
			]


targets = ['target_prod_rolling_7', 'target_style_rolling_7','target_prod_rolling_3', 'target_style_rolling_3','target_prod_rolling_1', 'target_style_rolling_1']

df = pd.DataFrame()

for t in targets:
	data = data[data[t] != -9999]

for t in targets:
	for f in features:

		plt.Figure()
		plt.plot(data[f], data[t], 'b.')
		plt.ylabel(t)
		plt.xlabel(f)
		plt.savefig('C:/P5GIT/' + f +'_'+ t + '.png')
		plt.close()

