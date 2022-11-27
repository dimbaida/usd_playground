from pxr import Usd

stage = Usd.Stage.Open('usd_models/transforms_issue.prime.usda')

prim = stage.GetPrimAtPath('/meshes')

for i in stage.Traverse():


