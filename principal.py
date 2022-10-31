import orbita_cy
import orbita_py
import time

ini_time=time.time()
orbita_cy.main()
fin_time= time.time()

time_cython =fin_time-ini_time

ini_time=time.time()
orbita_py.main()
fin_time= time.time()

time_python =fin_time-ini_time

print("Cython time: "+str(time_cython)+" seg")
print("Python time: "+str(time_python)+" seg")
print("Cython es "+str(time_python/time_cython)+"más rapido.")
print("\n")