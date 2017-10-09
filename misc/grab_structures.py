# Copy structures from storage into a local folder

import os
import shutil

source_folder = "/media/shares/Research-Groups/Yiliang-Ding/data_analysis_Ding_2013/MAC/Yin/Mapping_F/raw_data/"

dest_folder = os.path.expanduser( "~/foldatlas/source_data/structures" )

# genes_to_grab = {'AT1G01010', 'AT1G01020', 'AT1G01030', 'AT1G01040', 'AT1G01046', 'AT1G01050', 'AT1G01060', 'AT1G01070', 'AT1G01073', 'AT1G01080', 'AT1G01090', 'AT1G01100', 'AT1G01110', 'AT1G01115', 'AT1G01120', 'AT1G01130', 'AT1G01140', 'AT1G01150', 'AT1G01160', 'AT1G01170', 'AT1G01180', 'AT1G01183', 'AT1G01190', 'AT1G01200', 'AT1G01210', 'AT1G01220', 'AT1G01225', 'AT1G01230', 'AT1G01240', 'AT1G01250', 'AT1G01260', 'AT1G01270', 'AT1G01280', 'AT1G01290', 'AT1G01300', 'AT1G01305', 'AT1G01310', 'AT1G01320', 'AT1G01340', 'AT1G01350', 'AT1G01355', 'AT1G01360', 'AT1G01370', 'AT1G01380', 'AT1G01390', 'AT1G01400', 'AT1G01410', 'AT1G01420', 'AT1G01430', 'AT1G01440', 'AT1G01448', 'AT1G01450', 'AT1G01453', 'AT1G01460', 'AT1G01470', 'AT1G01471', 'AT1G01480', 'AT1G01490', 'AT1G01500', 'AT1G01510', 'AT1G01520', 'AT1G01530', 'AT1G01540', 'AT1G01550', 'AT1G01560', 'AT1G01570', 'AT1G01580', 'AT1G01590', 'AT1G01600', 'AT1G01610', 'AT1G01620', 'AT1G01630', 'AT1G01640', 'AT1G01650', 'AT1G01660', 'AT1G01670', 'AT1G01680', 'AT1G01690', 'AT1G01695', 'AT1G01700', 'AT1G01710', 'AT1G01720', 'AT1G01725', 'AT1G01730', 'AT1G01740', 'AT1G01750', 'AT1G01760', 'AT1G01770', 'AT1G01780', 'AT1G01790', 'AT1G01800', 'AT1G01810', 'AT1G01820', 'AT1G01830', 'AT1G01840', 'AT1G01860', 'AT1G01870', 'AT1G01880', 'AT1G01890', 'AT1G01900', 'AT1G01910', 'AT2G01010', 'AT2G01020', 'AT2G01021', 'AT2G01023', 'AT2G01050', 'AT2G01060', 'AT2G01070', 'AT2G01080', 'AT2G01090', 'AT2G01100', 'AT2G01110', 'AT2G01120', 'AT2G01130', 'AT2G01140', 'AT2G01150', 'AT2G01160', 'AT2G01170', 'AT2G01175', 'AT2G01180', 'AT2G01190', 'AT2G01200', 'AT2G01210', 'AT2G01220', 'AT2G01240', 'AT2G01250', 'AT2G01260', 'AT2G01270', 'AT2G01275', 'AT2G01280', 'AT2G01290', 'AT2G01300', 'AT2G01310', 'AT2G01320', 'AT2G01330', 'AT2G01340', 'AT2G01350', 'AT2G01360', 'AT2G01370', 'AT2G01390', 'AT2G01400', 'AT2G01410', 'AT2G01420', 'AT2G01422', 'AT2G01430', 'AT2G01440', 'AT2G01450', 'AT2G01460', 'AT2G01470', 'AT2G01480', 'AT2G01490', 'AT2G01500', 'AT2G01505', 'AT2G01510', 'AT2G01520', 'AT2G01530', 'AT2G01540', 'AT2G01554', 'AT2G01560', 'AT2G01570', 'AT2G01580', 'AT2G01590', 'AT2G01600', 'AT2G01610', 'AT2G01620', 'AT2G01630', 'AT2G01640', 'AT2G01650', 'AT2G01660', 'AT2G01667', 'AT2G01670', 'AT2G01680', 'AT2G01690', 'AT2G01710', 'AT2G01720', 'AT2G01730', 'AT2G01735', 'AT2G01740', 'AT2G01750', 'AT2G01755', 'AT2G01760', 'AT2G01770', 'AT2G01780', 'AT2G01790', 'AT2G01800', 'AT2G01810', 'AT2G01818', 'AT2G01820', 'AT2G01830', 'AT2G01850', 'AT2G01860', 'AT2G01870', 'AT2G01880', 'AT2G01890', 'AT2G01900', 'AT2G01905', 'AT2G01910', 'AT2G01913', 'AT2G01918', 'AT2G01920', 'AT2G01930', 'AT3G01015', 'AT3G01020', 'AT3G01030', 'AT3G01040', 'AT3G01050', 'AT3G01060', 'AT3G01070', 'AT3G01080', 'AT3G01085', 'AT3G01090', 'AT3G01100', 'AT3G01120', 'AT3G01130', 'AT3G01140', 'AT3G01142', 'AT3G01150', 'AT3G01160', 'AT3G01170', 'AT3G01175', 'AT3G01180', 'AT3G01185', 'AT3G01190', 'AT3G01200', 'AT3G01202', 'AT3G01210', 'AT3G01220', 'AT3G01230', 'AT3G01240', 'AT3G01250', 'AT3G01260', 'AT3G01270', 'AT3G01280', 'AT3G01290', 'AT3G01300', 'AT3G01310', 'AT3G01311', 'AT3G01313', 'AT3G01316', 'AT3G01319', 'AT3G01320', 'AT3G01322', 'AT3G01323', 'AT3G01324', 'AT3G01325', 'AT3G01326', 'AT3G01327', 'AT3G01328', 'AT3G01329', 'AT3G01330', 'AT3G01331', 'AT3G01340', 'AT3G01345', 'AT3G01350', 'AT3G01360', 'AT3G01370', 'AT3G01380', 'AT3G01390', 'AT3G01400', 'AT3G01410', 'AT3G01420', 'AT3G01430', 'AT3G01435', 'AT3G01440', 'AT3G01450', 'AT3G01460', 'AT3G01470', 'AT3G01472', 'AT3G01480', 'AT3G01490', 'AT3G01500', 'AT3G01510', 'AT3G01513', 'AT3G01516', 'AT3G01520', 'AT3G01530', 'AT3G01540', 'AT3G01550', 'AT3G01560', 'AT3G01570', 'AT3G01572', 'AT3G01580', 'AT3G01590', 'AT3G01600', 'AT3G01610', 'AT3G01620', 'AT3G01630', 'AT3G01640', 'AT3G01650', 'AT3G01660', 'AT3G01670', 'AT3G01680', 'AT3G01690', 'AT3G01700', 'AT3G01705', 'AT3G01710', 'AT3G01720', 'AT3G01730', 'AT3G01740', 'AT3G01750', 'AT3G01760', 'AT4G00020', 'AT4G00026', 'AT4G00030', 'AT4G00040', 'AT4G00050', 'AT4G00060', 'AT4G00070', 'AT4G00080', 'AT4G00085', 'AT4G00090', 'AT4G00100', 'AT4G00110', 'AT4G00120', 'AT4G00124', 'AT4G00130', 'AT4G00140', 'AT4G00150', 'AT4G00160', 'AT4G00165', 'AT4G00170', 'AT4G00180', 'AT4G00190', 'AT4G00200', 'AT4G00210', 'AT4G00220', 'AT4G00230', 'AT4G00231', 'AT4G00232', 'AT4G00234', 'AT4G00238', 'AT4G00240', 'AT4G00250', 'AT4G00260', 'AT4G00270', 'AT4G00280', 'AT4G00290', 'AT4G00300', 'AT4G00305', 'AT4G00310', 'AT4G00315', 'AT4G00320', 'AT4G00330', 'AT4G00335', 'AT4G00340', 'AT4G00342', 'AT4G00350', 'AT4G00355', 'AT4G00360', 'AT4G00370', 'AT4G00380', 'AT4G00390', 'AT4G00400', 'AT4G00416', 'AT4G00420', 'AT4G00430', 'AT4G00440', 'AT4G00450', 'AT4G00460', 'AT4G00467', 'AT4G00480', 'AT4G00490', 'AT4G00500', 'AT4G00520', 'AT4G00525', 'AT4G00530', 'AT4G00540', 'AT4G00550', 'AT4G00560', 'AT4G00570', 'AT4G00580', 'AT4G00585', 'AT4G00590', 'AT4G00600', 'AT4G00610', 'AT4G00620', 'AT4G00630', 'AT4G00650', 'AT4G00651', 'AT4G00660', 'AT4G00670', 'AT4G00680', 'AT4G00690', 'AT4G00695', 'AT4G00700', 'AT4G00710', 'AT4G00720', 'AT4G00730', 'AT4G00740', 'AT4G00750', 'AT4G00752', 'AT4G00755', 'AT4G00760', 'AT4G00770', 'AT4G00780', 'AT4G00800', 'AT4G00810', 'AT4G00820', 'AT4G00830', 'AT4G00840', 'AT4G00850', 'AT5G01015', 'AT5G01020', 'AT5G01030', 'AT5G01040', 'AT5G01050', 'AT5G01060', 'AT5G01070', 'AT5G01075', 'AT5G01080', 'AT5G01090', 'AT5G01100', 'AT5G01110', 'AT5G01120', 'AT5G01130', 'AT5G01140', 'AT5G01150', 'AT5G01160', 'AT5G01170', 'AT5G01175', 'AT5G01180', 'AT5G01190', 'AT5G01200', 'AT5G01210', 'AT5G01215', 'AT5G01220', 'AT5G01225', 'AT5G01230', 'AT5G01240', 'AT5G01250', 'AT5G01260', 'AT5G01270', 'AT5G01280', 'AT5G01290', 'AT5G01300', 'AT5G01310', 'AT5G01320', 'AT5G01330', 'AT5G01340', 'AT5G01350', 'AT5G01360', 'AT5G01365', 'AT5G01370', 'AT5G01380', 'AT5G01390', 'AT5G01400', 'AT5G01410', 'AT5G01420', 'AT5G01430', 'AT5G01440', 'AT5G01445', 'AT5G01450', 'AT5G01460', 'AT5G01470', 'AT5G01480', 'AT5G01490', 'AT5G01500', 'AT5G01510', 'AT5G01520', 'AT5G01530', 'AT5G01540', 'AT5G01542', 'AT5G01550', 'AT5G01560', 'AT5G01570', 'AT5G01580', 'AT5G01590', 'AT5G01595', 'AT5G01600', 'AT5G01610', 'AT5G01620', 'AT5G01630', 'AT5G01640', 'AT5G01650', 'AT5G01660', 'AT5G01670', 'AT5G01680', 'AT5G01690', 'AT5G01700', 'AT5G01710', 'AT5G01712', 'AT5G01720', 'AT5G01730', 'AT5G01732', 'AT5G01734', 'AT5G01740', 'AT5G01747', 'AT5G01750', 'AT5G01760', 'AT5G01770', 'AT5G01780', 'AT5G01790', 'AT5G01800', 'AT5G01810', 'AT5G01820', 'AT5G01830', 'AT5G01840', 'AT5G01849', 'AT5G01850', 'AT5G01860', 'AT5G01870'}

genes_to_grab = { "AT3G29370.1", "AT3G48550.1", "AT2G31360.1" }


def process_folder( source_folder, dest_folder ):
    files = os.listdir( source_folder )
    for filename in files:
        for gene in genes_to_grab:
            if gene in filename:
                source = source_folder + "/" + filename
                dest = dest_folder + "/" + filename
                shutil.copyfile( source, dest )
                print( "Added [" + dest + "]" )


process_folder( source_folder + "/in_silico_structures", dest_folder + "/in_silico" )
process_folder( source_folder + "/in_vivo_structures", dest_folder + "/in_vivo" )
